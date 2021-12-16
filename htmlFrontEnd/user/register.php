<?php
/*
 * @Author: your name
 * @Date: 2021-07-07 00:02:26
 * @LastEditTime: 2021-07-10 02:19:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \WWW\user\register.php
 */

include_once("functions/System.php");
include_once("functions/database.php");
if (empty($_POST)) {
    exit("您提交的表单数据超过post_max_size的配置！<br/>");
}
$password = $_POST['password'];
$confirmPassword = $_POST['confirmPassword'];
if ($password != $confirmPassword) {
    exit("输入的密码和确认密码不相等！");
}
$userName = $_POST['userName'];
$domain = $_POST['domain'];
$userName = $userName . $domain;
//判断用户名是否占用 
$userNameSQL = "select * from users where userName='$userName'";
getConnection();

$databaseConnection = mysqli_connect('10.122.201.99','root', 'root');

mysqli_select_db($databaseConnection, 'register');
$resultSet = mysqli_query($databaseConnection,$userNameSQL);
if (mysqli_num_rows($resultSet) > 0) {
    closeConnection();
    exit("用户名已经被占用，请更换其他用户名！");
}
//收集用户其他信息 
$sex = $_POST['sex'];
if (empty($_POST['interests'])) {
    $interests = "";
} else {
    $interests = implode(";", $_POST['interests']);
}
$remark = $_POST['remark'];
$myPictureName = $_FILES['myPicture']['name'];
//只有“文件上传成功”或“没有上传附件”时，才进行注册 

$registerSQL = "insert into users values(null,'$userName','$password','$sex','$myPictureName','$remark')";
$message = upload($_FILES['myPicture'], "uploads");
if ($message == "文件上传成功！" || $message == "没有选择上传附件！") {
    mysqli_query($databaseConnection,$registerSQL);
    $userID = mysqli_insert_id($databaseConnection);
    session_start();
    $_SESSION['userID'] = $userID;

    // echo "用户信息成功注册！<br/><br/><br/>";
} else {
    exit($message);
}
//从数据库中提取用户注册信息 

$userSQL = "select * from users where user_id=$userID";
$userResult = mysqli_query($databaseConnection,$userSQL);

$user = mysqli_fetch_array($userResult); 

// echo "您注册的用户名为：" . $user["userName"] . "<br/><br/>";
// echo "您填写的登录密码为：" . $user["password"] . "<br/><br/>";
// echo "性别：" . $user["sex"] . "<br/><br/>";
// echo "爱好：" . $user["interests"] . "<br/>。<br/>";
// $pictureAdrees = "uploads/" . $myPictureName;
// echo "上传的照片：";
// echo '<img src="' . $pictureAdrees . '"  width="200px">';
// echo "<br/><br/>";
// echo "备注信息：" . $user['remark'];
echo "<script>alert('恭喜！用户注册成功！')</script>";


header("refresh:1;url=http://localhost/user/login.html"); 
//     {
//     exit("用户信息注册失败！");
// }
closeConnection();
?>