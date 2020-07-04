<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/form.css">
  <script type="text/javascript" src="js/mask.js"></script>
  <title>Add Contact</title>
</head>

<body>
  <form name="add-contact" action="/add-contact" method="GET" onsubmit="return validateForm(this)" class="card center-card">
      <div class="container">
        <button>
          <a href="/">VOLTAR</a>
        </button>
        <hr>
        <input type="text" placeholder="Nome" name="name">
        <input type="text" placeholder="CPF" name="id" maxlength="14" onkeypress="idMask(this)">
        <input type="email" placeholder="Email" name="email">
        <input type="text" placeholder="Telefone" name="phone" maxlength="15" onkeypress="phoneMask(this)">
        <input type="submit" name="button" value="GRAVAR">
        <p id="message"></p>
      </div>
  </form>
</body>

</html>