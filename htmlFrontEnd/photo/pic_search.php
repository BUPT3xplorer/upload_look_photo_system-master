<?php 

$pic_types=$_POST['tags'];
$temp = explode(",",$pic_types);
$out_put="";
// echo $temp;
// print_r($temp);
if($temp[0] == 'ALL')
{
$temp=$filenames=scandir('pic_find');
array_splice($temp,0,1);
array_splice($temp,0,1);//delete ./ and ../
}
for($index_1=0;$index_1<count($temp);$index_1++)
{
$pic_type=$temp[$index_1];
// echo $pic_type;
$pic_file='pic_find/'.$pic_type;
$filenames=scandir($pic_file);
// print_r($filenames);
for($i=2;$i<count($filenames);$i++)
{
    $s=$pic_file.'/'.$filenames[$i];
    $pic='<img src="'.$s.'" height="200" width="220" >';
    $out_put=$out_put.$pic;
}
// echo $out_put;
}

$head='  <head>
<title>Bootstrap 4 Website Example</title>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link
  rel="stylesheet"
  href="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/css/bootstrap.min.css"
/>
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
<div class="jumbotron text-center" style="margin-bottom: 0">
  <h1>照片存储&展示</h1>
  <p>Pic_show</p>
</div>
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#collapsibleNavbar"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
      <a class="nav-link" href="http://localhost/flag.html"
      >用户界面</a
      >
     </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost/pachong/pachong.php"
          >网络爬虫</a
        >
      </li>
      <li class="nav-item">
        <a class="nav-link" href="http://localhost:5000/"
          >图片识别&分类存储</a
        >
      </li>

    </li>
    <li class="nav-item">
      <a class="nav-link" href="http://localhost/photo/pic_search.html"
        >图像综合查询</a
      >
    </li>
    </ul>
  </div>
</nav>';

$head= $head.$out_put.'</body>';


echo $head;



?>
