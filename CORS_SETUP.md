# Configuración de CORS

## ✅ CORS Configurado

El backend FastAPI ahora tiene configurado el middleware de CORS para permitir requests desde el frontend.

## 🔧 Configuración Actual

### Orígenes Permitidos por Defecto

- `http://localhost:3000` - Frontend en desarrollo local
- `http://127.0.0.1:3000` - Alternativa localhost
- `http://localhost:3001` - Alternativa puerto
- `http://127.0.0.1:3001` - Alternativa puerto

### Configuración del Middleware

- **allow_credentials**: `True` - Permite enviar cookies y headers de autenticación
- **allow_methods**: `GET, POST, PUT, DELETE, PATCH, OPTIONS` - Todos los métodos HTTP necesarios
- **allow_headers**: `*` - Permite todos los headers (incluyendo `Authorization`)
- **expose_headers**: `*` - Expone todos los headers en la respuesta

## 🌐 Agregar Orígenes Adicionales

Si necesitas agregar más orígenes (por ejemplo, para producción), puedes usar la variable de entorno `CORS_ORIGINS`:

### En docker-compose.yml

```yaml
asisya_api:
  environment:
    - CORS_ORIGINS=http://tu-dominio.com,https://tu-dominio.com
```

### En archivo .env

```bash
CORS_ORIGINS=http://tu-dominio.com,https://tu-dominio.com
```

Los orígenes deben estar separados por comas.

## 🐛 Solución de Problemas

### Error: "CORS policy: No 'Access-Control-Allow-Origin' header"

**Causa**: El origen del frontend no está en la lista de orígenes permitidos.

**Solución**:

1. Verifica que el frontend esté corriendo en uno de los puertos permitidos (3000 o 3001)
2. Si usas un puerto diferente, agrega la variable de entorno `CORS_ORIGINS` con tu URL
3. Reinicia el servicio de la API después de cambiar la configuración

### Error: "CORS policy: Credentials flag is 'true'"

**Causa**: Estás intentando usar `allow_origins=["*"]` con `allow_credentials=True`, lo cual no está permitido por seguridad.

**Solución**: Ya está corregido en el código. Siempre se usan orígenes específicos cuando `allow_credentials=True`.

### El token no se envía en las requests

**Causa**: Puede ser un problema de CORS o de configuración del cliente HTTP.

**Solución**:

1. Verifica que `allow_credentials=True` esté configurado (✅ ya está)
2. Verifica que el frontend esté usando `withCredentials: true` en Axios (no necesario, el interceptor ya maneja esto)
3. Verifica que el header `Authorization` esté en `allow_headers` (✅ ya está con `*`)

## 📝 Verificación

Para verificar que CORS está funcionando correctamente:

1. Abre las herramientas de desarrollador del navegador (F12)
2. Ve a la pestaña "Network"
3. Realiza una request desde el frontend
4. Verifica que los headers de respuesta incluyan:
   - `Access-Control-Allow-Origin: http://localhost:3000`
   - `Access-Control-Allow-Credentials: true`
   - `Access-Control-Allow-Methods: GET, POST, PUT, DELETE, PATCH, OPTIONS`

## 🔄 Reiniciar el Servicio

Después de cambiar la configuración de CORS, reinicia el servicio de la API:

```bash
docker-compose restart asisya_api
```

O si estás ejecutando localmente:

```bash
# Detén el servidor (Ctrl+C) y vuelve a ejecutar
python -m uvicorn asisya_api.main:app --reload
```

## 📚 Referencias

- [FastAPI CORS Documentation](https://fastapi.tiangolo.com/tutorial/cors/)
- [MDN CORS Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
