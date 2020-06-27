<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/list_contacts.css">
  <link rel="stylesheet" href="styles/common.css">
  <title>Home</title>
</head>

<body>
  <div class="card center-card">
    <button>
      <a href="/add-contact">VOLTAR</a>
    </button>
    <hr>
    <table>
      <tr>
        <th>NOME</th>
        <th>IDADE</th>
        <th>SEXO</th>
      </tr>
      % for row in rows:
      <tr>
        % for col in row:
        <td>{{ col }}</th>
          % end
      </tr>
      % end
    </table>
  </div>
</body>

</html>