# Projektprüfung und Funktionstests
# Projektprüfung und Funktionstests

## Voraussetzungen

Stelle sicher, dass du die folgenden Voraussetzungen erfüllst:

- [ ] Node.js ist installiert
- [ ] Alle Abhängigkeiten sind installiert (`npm install`)
- [ ] Heroku CLI ist installiert

## Tests ausführen

Führe die folgenden Befehle aus, um sicherzustellen, dass dein Projekt korrekt ist und funktioniert:

1. **Linting**: Überprüfe den Code auf Stil- und Formatierungsfehler.
    ```bash
    npm run lint
    ```

2. **Unit Tests**: Führe Unit-Tests aus, um die Funktionalität einzelner Komponenten zu überprüfen.
    ```bash
    npm test
    ```

3. **Build**: Erstelle das Projekt, um sicherzustellen, dass es ohne Fehler kompiliert.
    ```bash
    npm run build
    ```

4. **Start**: Starte das Projekt, um sicherzustellen, dass es wie erwartet läuft.
    ```bash
    npm start
    ```

## Anwendung über Heroku laufen lassen

Führe die folgenden Schritte aus, um die Anwendung auf Heroku zu deployen:

1. **Heroku Login**: Melde dich bei Heroku an.
    ```bash
    heroku login
    ```

2. **Heroku App erstellen**: Erstelle eine neue Heroku-App.
    ```bash
    heroku create
    ```

3. **Deploy**: Push das Projekt zu Heroku.
    ```bash
    git push heroku main
    ```

4. **Datenbank migrieren (falls erforderlich)**: Führe Datenbankmigrationen durch.
    ```bash
    heroku run npm run migrate
    ```

5. **Anwendung öffnen**: Öffne die Anwendung im Browser.
    ```bash
    heroku open
    ```

## Fehlerbehebung

Falls Fehler auftreten, überprüfe die Konsolenausgaben und behebe die gemeldeten Probleme. Weitere Informationen findest du in der Dokumentation oder im Fehlerprotokoll.

(venv) PS C:\Users\Petre\pflege-app> git push heroku main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Updated 70 paths from 506d6d1
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-22 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Using Python version specified in runtime.txt
remote: 
remote:  !     Error: Requested runtime '<<<<<<< HEAD
remote:  !     python-3.12.6
remote:  !     =======
remote:  !     python-3.12.6
remote:  !     >>>>>>> ed98b7f30a24b6c34c59a55b7f52e8a017c3edb5' is not available for this stack (heroku-22).
remote:  !     
remote:  !     For a list of the supported Python versions, see:
remote:  !     https://devcenter.heroku.com/articles/python-support#supported-runtimes
remote:
remote:  !     Push rejected, failed to compile Python app.
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: 69615be0e8e9176f4740e4e61c844857d465e14a
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version 69615be0e8e9176f4740e4e61c844857d465e14a
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !     git push heroku <branchname>:main
remote:  ! 
remote:  ! For more information, see:
remote:  !     https://devcenter.heroku.com/articles/git#deploying-code
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/your-app.git
 * [new branch]      main -> main
```

```markdown
# Projektprüfung und Funktionstests

## Voraussetzungen

Stelle sicher, dass du die folgenden Voraussetzungen erfüllst:

- [ ] Node.js ist installiert
- [ ] Alle Abhängigkeiten sind installiert (`npm install`)
- [ ] Heroku CLI ist installiert

## Tests ausführen

Führe die folgenden Befehle aus, um sicherzustellen, dass dein Projekt korrekt ist und funktioniert:

1. **Linting**: Überprüfe den Code auf Stil- und Formatierungsfehler.
    ```bash

    ```markdown
    # Projektprüfung und Funktionstests

    ## Voraussetzungen

    Stelle sicher, dass du die folgenden Voraussetzungen erfüllst:

    - [ ] Node.js ist installiert
    - [ ] Alle Abhängigkeiten sind installiert (`npm install`)
    - [ ] Heroku CLI ist installiert

    ## Tests ausführen

    Führe die folgenden Befehle aus, um sicherzustellen, dass dein Projekt korrekt ist und funktioniert:

    1. **Linting**: Überprüfe den Code auf Stil- und Formatierungsfehler.
        ```bash
        npm run lint
        ```
        

    2. **Unit Tests**: Führe Unit-Tests aus, um die Funktionalität einzelner Komponenten zu überprüfen.
        ```bash
        npm test
        ```

    3. **Build**: Erstelle das Projekt, um sicherzustellen, dass es ohne Fehler kompiliert.
        ```bash
        npm run build
        ```

    4. **Start**: Starte das Projekt, um sicherzustellen, dass es wie erwartet läuft.
        ```bash
        npm start
        ```

    ## Anwendung über Heroku laufen lassen

    Führe die folgenden Schritte aus, um die Anwendung auf Heroku zu deployen:

    1. **Heroku Login**: Melde dich bei Heroku an.
        ```bash
        heroku login
        ```

    2. **Heroku App erstellen**: Erstelle eine neue Heroku-App.
        ```bash
        heroku create
        ```

    3. **Deploy**: Push das Projekt zu Heroku.
        ```bash
        git push heroku main
        ```

    4. **Datenbank migrieren (falls erforderlich)**: Führe Datenbankmigrationen durch.
        ```bash
        heroku run npm run migrate
        ```

    5. **Anwendung öffnen**: Öffne die Anwendung im Browser.
        ```bash
        heroku open
        ```

    ## Fehlerbehebung

    Falls Fehler auftreten, überprüfe die Konsolenausgaben und behebe die gemeldeten Probleme. Weitere Informationen findest du in der Dokumentation oder im Fehlerprotokoll.

    (venv) PS C:\Users\Petre\pflege-app> git push heroku main
    Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Updated 70 paths from 506d6d1
    remote: Compressing source files... done.
    remote: Building source:
    remote: 
    remote: -----> Building on the Heroku-22 stack
    remote: -----> Using buildpack: heroku/python
    remote: -----> Python app detected
    remote: -----> Using Python version specified in runtime.txt
    remote: 
    remote:  !     Error: Requested runtime '<<<<<<< HEAD
    remote:  !     python-3.12.6
    remote:  !     =======
    remote:  !     python-3.12.6
    remote:  !     >>>>>>> ed98b7f30a24b6c34c59a55b7f52e8a017c3edb5' is not available for this stack (heroku-22).
    remote:  !     
    remote:  !     For a list of the
    ```

2. **Unit Tests**: Führe Unit-Tests aus, um die Funktionalität einzelner Komponenten zu überprüfen.
    ```bash
    npm test
    ```

3. **Build**: Erstelle das Projekt, um sicherzustellen, dass es ohne Fehler kompiliert.
    ```bash
    npm run build
    ```

4. **Start**: Starte das Projekt, um sicherzustellen, dass es wie erwartet läuft.
    ```bash
    npm start
    ```

## Anwendung über Heroku laufen lassen

Führe die folgenden Schritte aus, um die Anwendung auf Heroku zu deployen:

1. **Heroku Login**: Melde dich bei Heroku an.
    ```bash
    heroku login
    ```

2. **Heroku App erstellen**: Erstelle eine neue Heroku-App.
    ```bash
    heroku create
    ```

3. **Deploy**: Push das Projekt zu Heroku.
    ```bash
    git push heroku main
    ```

4. **Datenbank migrieren (falls erforderlich)**: Führe Datenbankmigrationen durch.
    ```bash
    heroku run npm run migrate
    ```

5. **Anwendung öffnen**: Öffne die Anwendung im Browser.
    ```bash
    heroku open
    ```

## Fehlerbehebung

Falls Fehler auftreten, überprüfe die Konsolenausgaben und behebe die gemeldeten Probleme. Weitere Informationen findest du in der Dokumentation oder im Fehlerprotokoll.

(venv) PS C:\Users\Petre\pflege-app> git push heroku main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Updated 70 paths from 506d6d1
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-22 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Using Python version specified in runtime.txt
remote: 
remote:  !     Error: Requested runtime '<<<<<<< HEAD
remote:  !     python-3.12.6
remote:  !     =======
remote:  !     python-3.12.6
remote:  !     >>>>>>> ed98b7f30a24b6c34c59a55b7f52e8a017c3edb5' is not available for this stack (heroku-22).
remote:  !     
remote:  !     For a list of the supported Python versions, see:
remote:  !     https://devcenter.heroku.com/articles/python-support#supported-runtimes
remote:
remote:  !     Push rejected, failed to compile Python app.
remote:
remote:  !     Push failed
remote:  !
remote:  ! ## Warning - The same version of this code has already been built: 69615be0e8e9176f4740e4e61c844857d465e14a
remote:  !
remote:  ! We have detected that you have triggered a build from source code with version 69615be0e8e9176f4740e4e61c844857d465e14a
remote:  ! at least twice. One common cause of this behavior is attempting to deploy code from a different branch.
remote:  !
remote:  ! If you are developing on a branch and deploying via git you must run:
remote:  !
remote:  !     git push heroku <branchname>:mai
=======
# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

## Deploying to Heroku

Using resources for this example app counts towards your usage. [Delete your app](https://devcenter.heroku.com/articles/heroku-cli-commands#heroku-apps-destroy) and [database](https://devcenter.heroku.com/articles/heroku-postgresql#removing-the-add-on) as soon as you are done experimenting to control costs.

By default, apps use Eco dynos if you are subscribed to Eco. Otherwise, it defaults to Basic dynos. The Eco dynos plan is shared across all Eco dynos in your account and is recommended if you plan on deploying many small apps to Heroku. Learn more about our low-cost plans [here](https://blog.heroku.com/new-low-cost-plans).

Eligible students can apply for platform credits through our new [Heroku for GitHub Students program](https://blog.heroku.com/github-student-developer-program).

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out for instructions on how to deploy this app to Heroku and also run it locally.

Alternatively, you can deploy it using this Heroku Button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://www.heroku.com/deploy?template=https://github.com/heroku/python-getting-started)

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
>>>>>>> 0396f5cbcdd79cd974723349272e8b1935fce976
