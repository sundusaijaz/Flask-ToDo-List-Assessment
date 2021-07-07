<h1>Flask-ToDo-List-Assessment</h1>

To run the project, simply run the following commands in cmd.

1. In Command Prompt navigate to your project:
     ### cd ./todolist-assessment

2. Build docker container:  
    ### docker image build -t docker-flask-test . (don’t miss the last .) 
  
3. Run docker container:
    ### docker run -p 5000:5000 -d docker-flask-test
 
* Note: After running the above command flask server will start running in browser. 

4. To stop the container:
    ### docker container stop [ID] 
  
5. After stopping server just run:
    ### docker system prune
  * This will any remove stopped containers, unused volumes and networks, and dangling images.
