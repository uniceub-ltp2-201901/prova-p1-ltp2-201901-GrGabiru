def get_proff(cursor):
    cursor.execute(f'select nome from faculdade.professor')
    nomes = cursor.fetchall()
    cursor.close()
    return nomes

def get_data(cursor):
    cursor.execute(f'select datanasc, nomemae from faculdade.professor where idprof=1')
    data = cursor.fetchall()
    cursor.close()
    return data

def get_disciplinas(cursor):
    cursor.execute(f'select disciplina from faculdade.disciplinas where idprof=1')
    discilina = cursor.fetchall()
    cursor.close()
    return discilina

