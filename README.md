# Audio to Sign Language Translator
<ul>
<li> This project is implemented as a website. The user has to give audio input of English sentence which will be converted to Indian Sign Language (ISL) sentence. 
<li> The impaired user will be shown a video consisting of signs of words in ISL sentence.
<li> This is a demo project and can be further extended at production level.
<li> For working and other details of the project, refer <i>Project Report.pdf</i> file.
<li> For getting a gist of the project, refer <i>Project Demo.mp4</i> file.
</ul>

## Prerequisite
<ol>
<li> There should be Java 1.8 on your machine.
<li> If you have any other version of Java, install Java 1.8 version. No need to install previous version of Java.
<li> Download Stanford Core NLP zip file from <i>https://stanfordnlp.github.io/CoreNLP/</i>
</ol>

## Setting the project
<ol>
<li> Clone the project.
<li> In server.py file, on line 4, put your java bin path. Eg. C:/Program Files/Java/jdk1.8.0_241/bin/java.exe
<li> Make sure you have JAVAHOME path in your Environment Variables.
<li> Extract the Stanford Core NLP zip file which you downloaded in prerequisite.
<li> In your project folder, create a new folder named as "models".
<li> Open the extracted folder, copy the "stanford-corenlp-full" folder and paste it in "models" folder in your project directory.
</ol>

## How to run the project
<ol>
<li> Make sure you have an Internet connection and a Microphone attached with your machine.
<li> Open a command prompt/terminal and run "server.py" file. Leave this command prompt/terminal as it is.
<li> Open another command prompt/terminal and run "main.py" file.
<li> It will show the IP address in last line.Copy that IP address and paste it in Microsoft Edge browser or Internet Explorer Browser. Let the page load.
<li> Click "Speak" button and say the english sentence clearly in the mic.
<li> Come back to the second command prompt/terminal where you had run "main.py". You will se the sentence which you spoke just now.
<li> It will create the ISL sentence and the "result.mp4" video in "static" folder which is to be displayed.
<li> Come back to browser, click "Show Video button. Video will be played and the English and converted ISL sentence will be displayed.
<li> For giving another input, again click the "Speak" button.
</ol>



