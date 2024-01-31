def implementAPI(logs):
    results = []
    users = []
    passwords = []
    logados = []
    for i in range (0,len(logs)):
      if logs[i][0] == 'register':
        if logs[i][1] in users:
          results.append('Username already exists')
        else:
          results.append('Registered Successfully')
          users.append(logs[i][1])
          passwords.append(logs[i][2])
      elif logs[i][0] == 'login':
        if logs[i][1] in users:
          user_index = users.index(logs[i][1])
          if logs[i][2] == passwords[user_index]:
            results.append('Logged In Successfully')
            logados.append(logs[i][1])
          else:
            results.append('Login Unsuccessful')
        else:
          results.append('Login Unsuccessful')
      elif logs[i][0] == 'logout':
        if logs[i][1] in logados:
          results.append('Logged Out Successfully')
          logados.remove(logs[i][1])
        else:
          results.append('Logout Unsuccessful')
    return results


logs = [['register', 'david', 'david123'], ['register', 'adam', '1Adam1'], ['login', 'david', 'david123'], ['login' ,'adam', '1adam1'],['logout', 'david']]

print(implementAPI(logs))
