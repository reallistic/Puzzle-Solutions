<?php
LRU Cache
$CacheMax = 0;
$count =0;
$Cache = array();
function setBound($max){
   global $Cache, $CacheMax, $count;
   $CacheMax = $max;
   if($max === 0){
      $Cache = array();
      $count=0;
   }
   elseif($max < $count){
      array_splice($Cache, $max-$count);
      $count = $max;
   }
}

function setCache($k, $v){
   global $Cache, $CacheMax, $count;
   if(isset($Cache[$k])){
      unset($Cache[$k]);
   }
   $Cache = array($k => $v ) + $Cache;
   $count=count($Cache);
   if($count > $CacheMax){
     array_pop($Cache);
     $count--;
   }
}

function getCache($k){
   global $Cache;    
   doPrint((isset($Cache[$k])?$Cache[$k]:"NULL"));   
   if(($v=$Cache[$k]) != ""){
      unset($Cache[$k]);
      $Cache = array($k => $v ) + $Cache;
   }
}

function peekCache($k){
   global $Cache;
   doPrint((isset($Cache[$k])?$Cache[$k]:"NULL"));
}

function dumpCache(){
   global $Cache, $count;
   if(count($Cache) >0 ){
      $SortedCache= $Cache;
      ksort($SortedCache, SORT_STRING);
      foreach($SortedCache as $k => $v){
         doPrint($k . " " . $v); 
      }
   }
   
}

function doPrint($val){
   print($val."\n");
}

/********************   Main  *******************************/
fscanf(STDIN, "%d\n", $maxLines);
while(($line = trim(fgets(STDIN))) !="" && $maxLines-- > 0 ){
   $line = explode(" ",$line);
   switch($line[0]){
      case "BOUND":
         setBound(max(0,intval($line[1])));
      break;
      case "SET":
         setCache($line[1],$line[2]);
      break;
      case "GET":
         getCache($line[1]);
      break;
      case "PEEK":
         peekCache($line[1]);
      break;
      case "DUMP":
         dumpCache();
      break;
   }
}
?>