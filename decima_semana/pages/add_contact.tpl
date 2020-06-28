<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/common.css">
  <link rel="stylesheet" href="styles/add_contact.css">
  <title>Add Contact</title>
</head>

<body>
  <form action="/add-contact" method="GET" class="card center-card">
    <div class="container">
    <div style="display: inline-block;">
      <button>
        <a href="/">VOLTAR</a>
      </button>
      % if message:
        <p style="color: red;">{{ message }}</p>
      % end
      </div>
      <hr>
      <input type="text" placeholder="Qual é o seu nome?" name="name">
      <input type="number" placeholder="Que idade você tem?" name="age">
      <input type="text" placeholder="E o seu número de telefone?" name="contact">
      <input type="submit" name="button" value="GRAVAR">
    </div>
  </form>
</body>

</html>