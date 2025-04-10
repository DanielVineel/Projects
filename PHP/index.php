<?php
echo('

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        body{
            background-color: rgb(33, 20, 48);
            color:white
        }
        .main{
            background-color: black;
            height:300px;
            width:200px;
            position: relative;
            left:40%;
            top:100px;
            
            
        }
        a{
            color:aqua
        }
        .data{
            position: relative;
            margin-top:30px;
            margin-left:5%;
            width:100%;
            /* background-color: red; */
        }
        .data div{
            margin-top:25px;
            height: 25px;
            
        }
        input{
           position: relative;
           top:-6px;
            width:70%;
            height:25px;
            border:0px;
        }
        
        #submit{
            width:50%;
            margin-left:20%;
            margin-top:40px;
            position: relative;
            
            
        }
        #p{
           position: relative;
           left:50%;
           font-size: 10px;
           top:-30px;
        }
        .mail{
           margin-left: 3%;
            background-color: aliceblue;
            display: inline-block;
            height:27px;
            color:rgb(17, 17, 70)
        }
        .password{
           margin-left: 3%;
            color:rgb(12, 12, 54);
           background-color: aliceblue;
           display: inline-block;
           height:27px;

        }
    </style>
</head>
<body>

    <div class="main">
        <div class="data">
            <div>
            E-Mail: <br>
            <i class=" mail material-icons">mail</i><input type="text" id="mail" ><br>
       </div>
       <div>
            Password:<br>
        <i class=" password material-icons">lock</i><input type="password" id="pwd"><br>
           
          <div id="p"><a href="#">forget Password</a></div><br>
          </div>
       <div> <input type="submit" value="Submit" id="submit"></div>

        </div>

    </div>
    
</body>
</html>

')
?>