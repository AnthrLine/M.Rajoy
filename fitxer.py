import os
def get_last_n_lines(file_name, N):
    # Fer una llista buida
    list_of_lines = []
    # Obrir el fitxer per llegir en binari
    with open(file_name, 'rb') as read_obj:
        # Anar al final
        read_obj.seek(0, os.SEEK_END)
        buffer = bytearray()
        # Guardar la posició actual del cursor
        pointer_location = read_obj.tell()
        # Loop fins que el cursor arribi a dalt
        while pointer_location >= 0:
            # Anar a pointer_location
            read_obj.seek(pointer_location)
            # Canviar la ubicació del punter en -1
            pointer_location = pointer_location -1
            # Llegir el byte
            new_byte = read_obj.read(1)
            # saber si es el final
            if new_byte == b'\n':
                # Guarda la línea a la llista del principi
                list_of_lines.append(buffer.decode()[::-1])
                # Si està fet envia
                if len(list_of_lines) == N:
                    return list(reversed(list_of_lines))
                # Continuar per la següent línea.
                buffer = bytearray()
            else:
                buffer.extend(new_byte)
        if len(buffer) > 0:
            list_of_lines.append(buffer.decode()[::-1])
    return list(reversed(list_of_lines))