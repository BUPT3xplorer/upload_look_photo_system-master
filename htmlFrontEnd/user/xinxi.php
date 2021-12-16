<?php
/*
 * @Author: your name
 * @Date: 2021-07-08 13:47:13
 * @LastEditTime: 2021-07-10 23:36:00
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \WWW\user\xinxi.php
 */
include_once("functions/database.php");
getConnection();

session_start();
$databaseConnection = mysqli_connect('10.122.201.99','root', 'root');
mysqli_select_db($databaseConnection, 'register');
$userID = $_SESSION['userID'];

if($userID)
{
    $userNameSQL = "select * from users where user_id=$userID";
    // echo $_SESSION['userID'];

    $userResult = mysqli_query($databaseConnection,$userNameSQL);

    $user = mysqli_fetch_array($userResult); 

  

    $pictureAdrees = "uploads/" . $user['my_picture'];
   
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
      <title>用户个人模块</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
      <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
      <script src="https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js"></script>
      <script src="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
      <style>
      .fakeimg {
          height: 200px;
          background: #aaa;
      }
      </style>
    </head>
    <body>
    
    <div class="jumbotron text-center" style="margin-bottom:0">
      <h1>个人信息界面</h1>
      <p>我是一个用户鸭</p> 
    </div>
    
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
          <li class="nav-item">
          <a class="nav-link" href="http://localhost/user.html"
          >主页</a
          >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost/user/register.html"
              >注册</a
            >
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost/user/login.html">登录</a>
        
            
          </li>
          <li class="nav-item">
            <a class="navbar-brand" href="http://localhost/user/xinxi.php"
              >个人信息查询</a
            >
          </li>

        </ul>
      </div>
    </nav>
    
    <div class="container" style="margin-top:40px">
      <div class="row">
        <div class="col-sm-3">
          <h2>个人头像</h2>
          <div class="fakeimg">
            <img src="'.$pictureAdrees.'" height="250" width="255" style = "object-fit: cover" />
          </div>
          <br/>
          <br/>
          <br/>
          <p>网安！！！</p>
          <h3>相关链接</h3>
          <ul class="nav nav-pills flex-column">
            <li class="nav-item">
              <a class="nav-link " href="https://bupt3xplorer.github.io/">3xplorer博客</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://scss.bupt.edu.cn/">北京邮电大学网络空间学院</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://jwgl.bupt.edu.cn/jsxsd/framework/xsMain.jsp">教务系统</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="https://blog.csdn.net/resu09">reus博客</a>
            </li>
          </ul>
          <hr class="d-sm-none">
        </div>
        <div class="col-sm-8">
          <h2 align="center" >卑微的个人信息显示</h2>
          <h5>个人信息介绍</h5>

          <table border="1" style="width:725px;font-size:28px">
          <tr>
              <th>栏目</th>
              <th>栏目内容</th>
          </tr>
          <tr>
              <td>用户名</td>
              <td>'. $user["userName"] .'</td>
          </tr>
          <tr>
              <td>密码</td>
              <td>' . $user["password"] . '</td>
          </tr>
          <tr>
              <td>性别</td>
              <td>' . $user["sex"] . '</td>
          </tr>
          <tr>
            <td>备注信息</td>
            <td>'. $user['remark'].'</td>
    
            </tr>
      </table>

      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      
          <div class="fakeimg">
            <img src="sucai/by.jpg" height="300" width="730" />
          </div>
    
          <br>
          <br>
          <br>
          <br>
          <br>
          
         
        
          <p>这里是网络空间安全学院！！！</p>
          <br>
         
        </div>
      </div>
    </div>
    
    <div class="jumbotron text-center" style="margin-bottom:0">
      <p>这里到底部了哦</p>
    </div>
    
    </body>
    </html>';
}
else 
{
    echo "<script>alert('Sorry!你没有权限查看！')</script>";
    // echo $user['user_id'];
    // echo $_SESSION['userID'];
    header("refresh:1;url=http://localhost/user.html");
}

closeConnection();
