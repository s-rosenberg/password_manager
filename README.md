# Password Manager

## Objetivo

Crear una app de password manager usando [Django](https://www.djangoproject.com/)

- Utiliza el modelo User de django.contrib.auth
- Modelos definidos:
  - Saved Passwords
  - Sites

## TODO

### Views

- ~~Register~~
- ~~Login~~
- User
- Site
- Password

### Templates

- Navbar:
  - Acceso al home
  - Login / Logout
  - Register
- User Panel: muestra los sitios donde hay passwords guardadas
- Site Panel: user-passwords guardadas para cada sitio

### Forms

- ~~Guardar Password~~
- Cambiar Password
- ~~Login?~~
- ~~Register?~~

### Modificar

- Modificar views que estan por default en django.contrib.auth.urls (de esta manera tambien puedo quitar la view para logout y usar directamente la de django)
- View de saved passwords
