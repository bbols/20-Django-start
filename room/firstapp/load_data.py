from projectUII.firstapp.models import Room, Door
#shell django
room1 = Room(name='Podval')
room1.save()

door1 = Door(room=room1, title='Gruzin Dver',date_post='2023-08-28')
door1.save()