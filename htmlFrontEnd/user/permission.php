<?php

session_start();

$id = $_SESSION['userID'];
if ($id)
{
    header("refresh:1;url=http://localhost/flag.html"); 
}
else
{
    echo "<script>alert('Sorry! 你没有权限登录!')</script>";
    header("refresh:1;url=http://localhost/user.html"); 
}

?>