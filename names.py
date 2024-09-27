user_promt =  "Enter a TODD:\t"
todos = []
exit = True
while exit:
  user_Action = input("Type add , Show , exit or edit\t").strip().lower()
  
  match user_Action:
    case'add': 
        todo = input("enter a todo:\t")
        todos.append(todo)
    case'show'|'display' :
        for item in todos:
            #item.title()
            print(item)
    case 'edit':
        num = 0
        for item in todos:
            #item.title()
            num = num + 1
            print(num,".-\t"+item)
        number = int(input("Number of the todo edit\t"))
        existing_todo = todos[number-1]
        todos[number-1] = input("please enter a new TODO\t")
        for item in todos:
            #item.title()
            print(item)
    case 'exit': 
        exit = False
        break
    
        
print("bye")