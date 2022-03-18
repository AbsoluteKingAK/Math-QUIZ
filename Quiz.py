print('Welcome to the Python MATH Quiz!')
ans = input('Are you ready ? (Y/n) : ')
score = 0
total_questions = 5

if ans.lower()=='y':
    ans = input('Question 1 : Lets start of easy - What is 1+1? : ')
    if ans.lower() == '2' or ans.lower() == 'two':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    ans = input('Question 2 : That was too easy, a little harder - What is 20*6? : ')
    if ans.lower() == '120' or 'hundred and twenty' in ans.lower() or 'hundred twenty' in ans.lower():
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    ans = input('Question 3: What is 3+2*0? : ')
    if ans.lower() == '3' or ans.lower() == 'three':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')
    
    ans = input('Question 4: What is 5,732 in words? : ')
    if 'five thousand seven hundred thirty two' in ans.lower() or 'five thousand seven hundred and thirty two' in ans.lower():
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

    ans = input('Last Question: 2*(x+24) = 66. Find x : ')
    if ans.lower() == '9' or ans.lower() == 'nine':
        score += 1
        print('Correct!')
    else:
        print('Wrong Answer :(')

mark = (score/total_questions)*100
if score == 5:
    print('Thank you for playing, you got ALL questions correctly!')
    print('Marks obtained :',mark,'(Great job!)')
else :
    print('Thank you for playing, you got',score,'questions correctly!')
    print('Marks obtained :',mark)