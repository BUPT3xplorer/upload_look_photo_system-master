<?php
/*
 * @Author: your name
 * @Date: 2021-07-07 00:02:26
 * @LastEditTime: 2021-07-10 02:17:47
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \WWW\user\login.php
 */
include_once("functions/database.php");
//收集表单提交数据 
//收集表单提交数据 
// $userName = addslashes($_POST['userName']);
// $password = addslashes($_POST['password']);
$userName = ($_POST['userName']);
$password = ($_POST['password']);
//连接数据库服务器 
getConnection();

session_start();
//判断用户名和密码是否输入正确 
$databaseConnection = mysqli_connect('10.122.201.99', 'root', 'root');
mysqli_select_db($databaseConnection, 'register');
$sql = "select * from users where userName='$userName' and password='$password'";
$resultSet = mysqli_query($databaseConnection,$sql);
$user = mysqli_fetch_array($resultSet); 

$_SESSION['userID'] = $user['user_id'];


if (mysqli_num_rows($resultSet) > 0) {
    echo "<script>alert('用户账户密码正确，用户登录成功')</script>";
    // echo $user['user_id'];
    // echo $_SESSION['userID'];
    header("refresh:1;url=http://localhost/user.html");
    
} 
else {

    echo "<script>alert('用户名和密码输入错误！登录失败！')</script>";
    header("refresh:1;url=http://localhost/user/login.html");
}
closeConnection();
?>