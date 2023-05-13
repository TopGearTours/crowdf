<!DOCTYPE html>
<html>
<head>
  <title>Language Switcher</title>
  <script src="script.js"></script>
</head>
<body>
  <select id="language-select" onchange="changeLanguage(this.value)">
    <option value="sk">Slovensky</option>
    <option value="pl">Polski</option>
    <option value="cz">Čeština</option>
    <option value="de">Deutsch</option>
    <option value="en">English</option>
  </select>
  <div id="language-content"></div>
</body>
</html>
