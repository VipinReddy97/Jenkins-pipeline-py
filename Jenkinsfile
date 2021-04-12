pipeline {
//None parameter in the agent section means that no global agent will be allocated for the entire Pipeline’s
//execution and that each stage directive must specify its own agent section.
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    //This image parameter (of the agent section’s docker parameter) downloads the python:2-alpine
                    //Docker image and runs this image as a separate container. The Python container becomes
                    //the agent that Jenkins uses to run the Build stage of your Pipeline project.
                    image 'python:2-alpine'
                }
            }
            steps {
                //This sh step runs the Python command to compile your application and
                //its calc library into byte code files, which are placed into the sources workspace directory
                sh 'python -m py_compile pycalculator.py'
                //This stash step saves the Python source code and compiled byte code files from the sources
                //workspace directory for use in later stages.
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    //This image parameter downloads the qnib:pytest Docker image and runs this image as a
                    //separate container. The pytest container becomes the agent that Jenkins uses to run the Test
                    //stage of your Pipeline project.
                    image 'qnib/pytest'
                }
            }
            steps {
                //This sh step executes pytest’s py.test command on sources/test_calc.py, which runs a set of
                //unit tests (defined in test_calc.py) on the "calc" library’s add2 function.
                //The --junit-xml test-reports/results.xml option makes py.test generate a JUnit XML report,
                //which is saved to test-reports/results.xml
                sh 'py.test --verbose --junit-xml test-reports/results.xml pycalculator-unitest.py'
            }
            post {
                always {
                    //This junit step archives the JUnit XML report (generated by the py.test command above) and
                    //exposes the results through the Jenkins interface.
                    //The post section’s always condition that contains this junit step ensures that the step is
                    //always executed at the completion of the Test stage, regardless of the stage’s outcome.
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$/var/jenkins_home/workspace/Pipeline-Dockeragent/17'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F pycalculator.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/dist/pycalculator"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}  


