module.exports = {
    /**
   * Application configuration section
   * http://pm2.keymetrics.io/docs/usage/application-declaration/
   */
    deploy: {
        production: {
            user: 'user',  // Your user for authentication
            host: '999.99.999.99',  // Your server ip address
            ref: 'origin/master',  // branch to deploy
            repo: 'ssh-repo.git',  // Your repository ssh direction
            path: '/home/user/apps/my-app',  // Where the project is stored
            'post-deploy':  // Commands to execute after pull source code
                'docker stop  && ' +
                'docker rm my-app && ' +
                'docker build -t my-app:latest . && ' +
                'docker run -d -p 8098:5000 --name my-app my-app'
        }
    }
}
