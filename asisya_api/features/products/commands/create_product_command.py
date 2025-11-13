from mediatr import Mediator
from fastapi import UploadFile
from typing import Optional

from asisya_api.domain.product import ProductEntity
from asisya_api.features.products.models import ProductCreateDTO, ProductResponseDTO
from asisya_api.features.products.repository import ProductRepository

from asisya_api.core.config import settings
from asisya_api.crosscutting.logging import get_logger
from asisya_api.infrastructure.storage_service import S3Storage, LocalStorage

logger = get_logger(__name__)


class CreateProductCommand:
    def __init__(self, data: ProductCreateDTO, picture: Optional[UploadFile], user):
        self.data = data
        self.picture = picture
        self.user = user


@Mediator.handler
class CreateProductCommandHandler:
    def __init__(self):
        self.product_repository = ProductRepository.instance()
        self.storage = (
            S3Storage(settings.aws_s3_bucket, settings.aws_region)
            if settings.storage_backend == "s3"
            else LocalStorage()
        )

    def handle(self, request: CreateProductCommand) -> ProductResponseDTO:
        logger.info(f"User {request.user.id} creating product '{request.data.name}'")

        picture_key = None
        if request.picture:
            picture_key = self.storage.save(request.picture, prefix="products")

        product_entity = ProductEntity(
            name=request.data.name,
            slug=request.data.slug,
            description=request.data.description,
            price=request.data.price,
            units_in_stock=request.data.stock,
            category_id=request.data.category_id,
        )

        created_product = self.product_repository.create(product_entity)

        picture_url = (
            self.storage.get_url(created_product.picture_path)
            if created_product.picture_path
            else None
        )

        return ProductResponseDTO(
            id=created_product.id,
            name=created_product.name,
            slug=created_product.slug,
            description=created_product.description,
            price=created_product.price,
            stock=created_product.stock,
            picture_url=picture_url,
            category_id=created_product.category_id,
            created_at=created_product.created_at,
            updated_at=created_product.updated_at,
        )
