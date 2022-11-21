import sqlite3

base = sqlite3.connect('new.bd')
cur = base.cursor()

################################################################################
#CREATE
print("Створюємо таблицю...")
base.execute('CREATE TABLE IF NOT EXISTS {}(tasks, prior, data)'.format('db'))
base.commit()
print()
################################################################################
#INSERT
print("Додаємо данні у БД...")
cur.execute('INSERT INTO db VALUES(?, ?, ?)', ('Зробити 9-ту лабу', '1', '21-11-2020'))
base.commit()
cur.execute('INSERT INTO db VALUES(?, ?, ?)', ('Захистити 8-ту лабу', '1', '22-11-2022'))
base.commit()
cur.execute('INSERT INTO db VALUES(?, ?, ?)', ('Зіграти в оновлену The Witcher 3', '2', '12-12-2022'))
base.commit()
cur.execute('INSERT INTO db VALUES(?, ?, ?)', ('Переглянути фільм', '4', '29-11-2022'))
base.commit()
cur.execute('INSERT INTO db VALUES(?, ?, ?)', ('Відредагувати зображення avatarka23.png ', '4', '25-11-2022'))
base.commit()
print()

################################################################################
#SELECT

print("Виводимо всі данні записані у цю БД(у вигляді кортежів)...")
b = cur.execute('SELECT * FROM db').fetchall()
print(b)
print()
print("Виводимо всі данні з пріорітетністю 1...")
a = cur.execute('SELECT * FROM db WHERE prior == ?', ('1',)).fetchall()
print(a)
print()
################################################################################
#UPDATE
print("Оновлюємо дату здачі лаби номер 9...")
cur.execute('UPDATE db SET data == ? WHERE tasks == ?', ('21-11-2022', 'Зробити 9-ту лабу'))
base.commit()
print("Знову виводио всі данні...")
q = cur.execute('SELECT * FROM db').fetchall()
print(q)
print()
################################################################################
#DELETE

print("Видаляємо всі данні з пріорітетністю 4...")
cur.execute('DELETE FROM db WHERE prior == ?', ('4',))
base.commit()
e = cur.execute('SELECT * FROM db').fetchall()
print(e)
print()

print("Видаляємо всю таблицю...")
base.execute('DROP TABLE IF EXISTS db')
base.commit()
print()
#################################################################################
print("The End")
base.close()