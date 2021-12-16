<?php  
$databaseConnection = null; 
function getConnection(){ 
     $hostname = "10.122.201.99"; 			//数据库服务器主机名，可以用IP代替 
     $database = "register"; 				//数据库名 
     $userName = "root"; 				//数据库服务器用户名 
     $password = "root"; 					//数据库服务器密码 
     global $databaseConnection; 
     $databaseConnection = mysqli_connect($hostname, $userName, $password);//连接数据库服务器 
     mysqli_query($databaseConnection,"set names 'gbk'");	//设置字符集 
     mysqli_select_db($databaseConnection, $database); 
} 
function closeConnection(){ 
     global $databaseConnection; 
     if($databaseConnection){ 
     		mysqli_close($databaseConnection); 
     } 
} 
?>
