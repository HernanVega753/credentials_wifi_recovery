import subprocess


def credentials_recovery():
    #Obtener nombre de perfiles
    profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    #Extraer nombres de los perfiles
    profiles_names = []
    for i in profiles:
        if "Perfil de todos" in i:
            i = i.split(':')
            profiles_names.append(i[1].strip())

    #Mostrar contraseña
    for profile in profiles_names:
        resultado = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode(
            'ISO.8859-1').split('\n')
        contrasenias = [line.split(':')[1].strip() for line in resultado if 'Contenido de la clave' in line]
        print(f'wifi:{profile} : password:{contrasenias[0] if contrasenias else "Password not found"}')


credentials_recovery()
