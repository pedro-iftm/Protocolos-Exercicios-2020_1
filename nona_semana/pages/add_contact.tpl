<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/add_contact.css">
  <link rel="stylesheet" href="styles/common.css">
  <title>Login</title>
</head>

<body>
  <nav>
    <p>Bem-vindo</p>
  </nav>
  <form action="/add-contact" method="GET" class="card center-card">
    <div class="container">
      <input type="text" placeholder="Qual é o seu nome?" name="name">
      <input type="number" placeholder="Que idade você tem?" name="age">
      <input type="text" placeholder="E o seu gênero?" name="gender">
      <input type="submit" name="button" value="GRAVAR">
      % if message:
        <p style="color: red;">{{ message }}</p>
      % end
    </div>
  </form>
</body>

</html>