count=0
def HF():
    f=open('hf.txt','w')
    f.write('1.When did they open the London underground?\n')
    f.write('2.Who invented the World Wide Web, and when?\n')
    f.write('3.What happened on July 20th, 1969?\n')
    f.write('4.When was the first issue of Vogue published: 1892, 1960, 2000?\n')
    f=open('hf.txt','r')
    hf_quiz=list(f)
    global count
    try:
        for i in hf_quiz:
            print(i)
            ans=input('answer:')
            if ans=='1863':
                count=count+1
            elif ans=='1990':
                count+=1
            elif ans=='1920':
                count+=1
            elif ans=='Apollo 11':
                count+=1    
            else:
                print('wrong\n')
    except Exception as e:
        print(e)
    finally:
        print('you can continue quiz')

def PCM():
    f=open('pcm.txt','w')
    f.write('1.Where is Billie Eilish from?\n')
    f.write('2.What city do The Beatles come from?\n')
    f.write('3.What is the all-time most-streamed song on Spotify to date?\n')
    f.write('4.What is the most-streamed album on Spotify in 2019?\n')
    f.write('5.How many keys does a classic piano have?\n')
    f.write('6.Which famous American pop band was originally called ‘Kara’s Flowers’?\n')
    f=open('pcm.txt','r')
    pcm_quiz=list(f)
    global count
    try:
        for i in pcm_quiz:
            print(i)
            ans=input('answer:')
            if ans=='los angeles':
                count=count+1
            elif ans=='Liverpool':
                count+=1
            elif ans=='EdSheeran':
                count+=1
            elif ans=='BillieEilish':
                count+=1
            elif ans=='88':
                count+=1
            elif ans=='Maroon5':
                count+=1  
            else:
                print('wrong\n')
    except Exception as e:
       print(e)
    finally:
        print('you can continue quiz')

def sports():
    f=open('sports.txt','w')
    f.write('1.Where was the first modern Olympic Games held?\n')
    f.write('2.Which football team is known as ‘The Red Devils’?\n')
    f.write('3.Which driver has won the most Formula 1 championships?\n')
    f.write('4.Who is 3rd on the all-time list of female tennis Grand Slam champions?\n')
    f.write('5.What was the clothing company Nike originally called?\n')
    f=open('sports.txt','r')
    sports_quiz=list(f)
    global count
    try:
        for i in sports_quiz:
            print(i)
            ans=input('answer:')
            if ans=='1896':
                count=count+1
            elif ans=='Manchester United':
                count+=1
            elif ans=='Serena Williams':
                count+=1
            elif ans=='Apollo 11':
                count+=1
            elif ans=='1892':
                count+=1
            else:
                print('wrong')
    except Exception as e:
       print(e)
    finally:
        print('you can continue quiz')


def FT():
    f=open('FT.txt','w')
    f.write('1.When was Netflix founded: 1997, 2001, 2009, 2015?\n')
    f.write('2.What was the most-watched series on Netflix in 2019?\n')
    f.write('3.Name Pixar’s first feature-length movie?\n')
    f.write('4.What is the name of the coffee shop in the sitcom Friends?\n')
    f.write('5.Name Disney’s first film?\n')
    f=open('FT.txt','r')
    ft_quiz=list(f)
    global count
    try:
        for i in ft_quiz:
            print(i)
            ans=input('answer:')
            if ans=='1997':
                count=count+1
            elif ans=='StrangerThings':
                count+=1
            elif ans=='1995':
                count+=1
            elif ans=='Central Perk':
                count+=1
            elif ans=='Blue Ribbon Sports':
                count+=1
            else:
                print('wrong')
    except Exception as e:
           print(e)
    finally:
        print('you can continue quiz')

while True:
    print('1.History & fashion')
    print('2.Pop culture & music')
    print('3.Sports')
    print('4.Film & TV')
    print('5.Exit')

    choice=int(input('Enter Choice:'))
    if choice==1:
        HF()
    elif choice==2:
        PCM()
    elif choice==3:
        sports()
    elif choice==4:
        FT()
    elif choice==5:
        print('Your total score is:',count)
        print('Thank You')
        break
    else:
        print('Wrong Choice')



