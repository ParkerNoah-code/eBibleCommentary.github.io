import os

def create_files_with_index(base_name, num_files):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    for i in range(1, num_files + 1):
        file_name = os.path.join(script_directory, f"{base_name}-{i}.html")
        with open(file_name, 'w') as file:
            file.write(html_content)

base_name = "evidences3"
num_files = 8
html_content = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="../../../style.css" />
    <script rel="script" type="text/javascript" src="../../../functions.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
        <h1>William Paley</h1>
      </header>

      <ul>
        <li>
          <a href="../../../index.html">About</a> |
          <a href="../../../Theology.html"> Theology</a> |
          <a href="../../../OTIntro.html"> Old Testament</a> |
          <a href="../../../NTIntro.html"> New Testament</a>
        </li>
      </ul>
      
      <section>
        <p>
          <a href="../../History.html">Theologians</a
          >: 
          <a href="evidences.html">Evidences of Christianity</a>
        </p>
      </section>

      <section>
        
      </section>

      <footer>
        <p>&copy; 2023 ebiblecommentary. All rights reserved.</p>
      </footer>
    </div>
  </body>
</html>
"""

create_files_with_index(base_name, num_files)