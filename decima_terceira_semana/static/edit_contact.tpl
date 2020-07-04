<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/form.css">
  <script type="text/javascript" src="js/mask.js"></script>
  <title>Edit Contact</title>
</head>

<body>
  <form action="/edit-contact" method="GET" class="card center-card">
    <div class="container">
      <button>
        <a href="/">VOLTAR</a>
      </button>
      <hr>
      <input type="text" placeholder="Nome" name="name" value="{{ name }}">
      <input type="text" placeholder="CPF" name="id" value="{{ id }}" readonly>
      <input type="text" placeholder="Email" name="email" value="{{ email }}">
      <input type="text" placeholder="Telefone" name="phone" value="{{ phone }}" maxlength="15" onkeypress="phoneMask(this)">
      <input type="submit" name="save_button" value="GRAVAR">
    </div>
  </form>
</body>

</html>