<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login</title>
</head>

<body>
  <p>Acesso negado</p>
  <table border="1">
    %for row in rows:
    <tr>
      %for col in row:
      <td>{{col}}</td>
      %end
    </tr>
    %end
  </table>
</body>

</html>