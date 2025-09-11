# Create project directory
mkdir zipchallenge
cd zipchallenge

# Initialize git repo
git init

# Create a more complex application structure
mkdir -p src/components src/utils src/assets config docs tests

# Create misleading app files
echo "#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)" > src/app.py

echo "/* Main application styles */
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f5f5f5;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
}
.hidden {
  display: none;
}" > src/assets/main.css

echo "<!DOCTYPE html>
<html>
<head>
  <title>Secure Application</title>
  <link rel='stylesheet' href='/assets/main.css'>
</head>
<body>
  <div class='container'>
    <h1>Welcome to the Secure App</h1>
    <p>This application contains important data.</p>
    <!-- Flag was here but moved for security reasons -->
  </div>
  <script src='/assets/main.js'></script>
</body>
</html>" > src/templates/index.html

echo "console.log('Application initialized');
// TODO: Implement security features
function checkFlag() {
  // Flag checking logic removed for security
  return false;
}" > src/assets/main.js

# Add and commit these files
git add .
git commit -m "Initial application setup"

# Add some misleading flags in various places
echo "# Configuration
DEBUG=True
SECRET_KEY=verysecretkey123
FLAG_LOCATION=/etc/secrets/flag.txt" > config/settings.conf
git add config/settings.conf
git commit -m "Add configuration settings"

# Add first part of the flag
echo "First part of the flag: MED{Z1P_" > .secret_part1
git add .secret_part1
git commit -m "Add temporary key file - REMOVE BEFORE PRODUCTION"

# Add more misleading files
echo "# Security Notes
- Make sure to encrypt all traffic
- Rotate keys every 30 days
- The flag was moved to the database
- Check security policy doc for details" > docs/security.md
git add docs/security.md
git commit -m "Add security documentation"

# Add a fake flag
echo "THIS_IS_NOT_THE_REAL_FLAG_KEEP_LOOKING" > flag.txt
git add flag.txt
git commit -m "Add flag file for testing"

# Add second part of flag
echo "CR4CK_" > .secret_part2
git add .secret_part2
git commit -m "Add encryption key part 2"

# Multiple commits with code changes to distract
echo "def authenticate(username, password):
    # TODO: Implement real authentication
    return username == 'admin' and password == 'password123'" > src/utils/auth.py
git add src/utils/auth.py
git commit -m "Add authentication utility - needs improvement"

# Update the file with slightly different code
echo "def authenticate(username, password):
    # TODO: Implement proper hashing
    import hashlib
    hashed_pw = hashlib.md5(password.encode()).hexdigest()
    return username == 'admin' and hashed_pw == '482c811da5d5b4bc6d497ffa98491e38'" > src/utils/auth.py
git add src/utils/auth.py
git commit -m "Update authentication with basic hashing"

# Add third part of flag
echo "D3FL4T3D_" > another_temp_file
git add another_temp_file
git commit -m "Temporary file for backup process"

# Add more code changes
echo "// Security module
function encryptData(data, key) {
  // Basic XOR encryption for demonstration
  return data.split('').map(char => 
    String.fromCharCode(char.charCodeAt(0) ^ key.charCodeAt(0))
  ).join('');
}" > src/utils/crypto.js
git add src/utils/crypto.js
git commit -m "Add frontend encryption utility"

# Add fourth part of flag and immediately remove it
echo "M4ST3R}" > final_key_fragment
git add final_key_fragment
git commit -m "Add final key part - REMOVE IMMEDIATELY"
git rm final_key_fragment
git commit -m "Remove sensitive data from repository"

# Add a database initialization script with a fake flag table
echo "-- Database initialization
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT,
  is_admin BOOLEAN
);

CREATE TABLE flags (
  id INTEGER PRIMARY KEY,
  flag TEXT,
  is_real BOOLEAN
);

INSERT INTO flags VALUES (1, 'NOT_THE_FLAG{NICE_TRY}', 0);
INSERT INTO flags VALUES (2, 'FAKE_FLAG{STILL_LOOKING}', 0);
-- Real flag removed and stored in separate secured storage" > db_init.sql
git add db_init.sql
git commit -m "Add database initialization script"

# Add README with misleading instructions
echo "# Secure Application

## Setup Instructions
1. Install dependencies: \`pip install -r requirements.txt\`
2. Initialize database: \`sqlite3 app.db < db_init.sql\`
3. Run the application: \`python src/app.py\`

## Finding the Flag
To find the flag, you need to:
1. Login as admin
2. Access the /admin/dashboard route
3. Solve the cryptographic challenge

Good luck!" > README.md
git add README.md
git commit -m "Update README with instructions"

# Remove some of the secret files to make it harder to find
git rm .secret_part1
git commit -m "Remove temporary files"
git rm .secret_part2
git commit -m "Cleanup old key files"
git rm another_temp_file
git commit -m "Remove unnecessary backup file"

# Add a misleading requirements file
echo "flask==2.0.1
sqlalchemy==1.4.23
cryptography==3.4.8
bcrypt==3.2.0
# Note: flagfinder package removed for security" > requirements.txt
git add requirements.txt
git commit -m "Add project dependencies"

# Create a password for the zip
ZIP_PASSWORD="challenge123"

# Create the zip file with ZipCrypto encryption
zip -r --password "$ZIP_PASSWORD" ../challenge.zip .

echo "ref: refs/heads/main" > plain_git_head.txt