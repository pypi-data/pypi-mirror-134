 # myprofile.py


class Profile:
    '''
        Example...
        my = Profile('Boat')
        my.company = ('Indeebrew')
        my.hobby = ('Gaming','Programing','Traveling')
        print(my.name)
        my.show_email()
        my.show_myart()
        my.show_hobby() 
    
    '''

    def __init__(self,name):
        self.name = name
        self.company = ''
        self.hobby = []     # ประกาศ hobby เป็น list เพื่อเก็บได้หลายค่า
        self.art = '''
             .-"""-.
            /       \.
            \       /
     .-"""-.-`.-.-.<  _
    /      _,-\O__O-_/ )  ~ Want some Beer?
    \     / ,  `   . `|
     '-..-| \-.,__~ ~ /          .,
           \ `-.__/  /          /"/
          / `-.__.-\`-._    ,",' ;
         / /|    ___\-._`-.; /  ./-.  
        ( ( |.-"`   `'\ '-( /  //.-' 
         \ \/  {.}{.}  |   /-. /.-'
          \|           /   '..' 
           \        , /
           ( __`;-;'__`)
           `//'`   `||`
          _//       ||
  .-"-._,(__)     .(__).-""-.
 /          \    /           \.
 \          /    \           /
  `'-------`      `--------'`
        
        '''

    def show_email(self):
        if self.company != '':
            print('{}@{}.com'.format(self.name.lower(),self.company.lower()))     # lower() คือทำให้เป็นตัวพิมพ์เล็กทั้งหมด
        else:
            print('{}@gmail.com'.format(self.name.lower()))

    def show_myart(self):
        print(self.art)

    def show_hobby(self):
        if len(self.hobby)!=0:                      # len เป็นคำสั่งให้นับ
            print('-------My Hobby-------')
            for i,h in enumerate(self.hobby,start=1):       # enumerate เป็นคำสั่งให้สร้างลำดับเลขขึ้นมาโดยเริ่มจาก1
                print(i,h)
            print('----------------------')
        else:
            print('No Hobby')

if __name__=='__main__':     # เงื่อนไขนี้ทำให้ ถ้าเรียกใช้ myprofile จากไฟล์อื่นจะไม่ run
    
    my = Profile('Tosachai')
    my.company = ('Indeebrew')
    my.hobby = ('Gaming','Watching Movie','Traveling')
    print(my.name)
    my.show_email()
    my.show_myart()
    my.show_hobby() 
    #help(my)



