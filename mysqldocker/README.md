### Docker Compose Configuration for MySQL and MySQL Workbench

#### Prerequisites:
- Docker installed on your machine. [Install Docker](https://docs.docker.com/desktop/install/windows-install/)

#### How to Use:
1. Download the `docker-compose.yml` file.
2. If you want to use any data, create a folder named `data` in the same directory.

3. Open CMD in the same directory and run:
   ```sh
   docker compose up
   ```
   Wait for the files to download and create.

### Usage:
1. Open MySQL Workbench at [http://localhost:3000/](http://localhost:3000/).
2. Connect to the database using:
   - Hostname: `mysql-container`
   - Username: `root`
   - Password: `admin`
3. To interact with MySQL from CMD, run:
   ```sh
   docker exec -it mysql-container mysql -uroot -p
   ```
4. To stop the containers, run:
   ```sh
   docker compose down
   ```
   Or stop it from the Docker program.
