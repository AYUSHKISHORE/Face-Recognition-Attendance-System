<?php

function multi_attach_mail($to, $subject, $message, $senderEmail, $senderName, $files = array()){ 
 
    $from = $senderName." <".$senderEmail.">";  
    $headers = "From: $from"; 
 
    $semi_rand = md5(time());  
    $mime_boundary = "==Multipart_Boundary_x{$semi_rand}x";  
 
    $headers .= "\nMIME-Version: 1.0\n" . "Content-Type: multipart/mixed;\n" . " boundary=\"{$mime_boundary}\"";  
 
    $message = "--{$mime_boundary}\n" . "Content-Type: text/html; charset=\"UTF-8\"\n" . 
    "Content-Transfer-Encoding: 7bit\n\n" . $message . "\n\n";  
 
    // Preparing attachment 
    if(!empty($files)){ 
        for($i=0;$i<count($files);$i++){ 
            if(is_file($files[$i])){ 
                $file_name = basename($files[$i]); 
                $file_size = filesize($files[$i]); 
                 
                $message .= "--{$mime_boundary}\n"; 
                $fp =    @fopen($files[$i], "rb"); 
                $data =  @fread($fp, $file_size); 
                @fclose($fp); 
                $data = chunk_split(base64_encode($data)); 
                $message .= "Content-Type: application/octet-stream; name=\"".$file_name."\"\n" .  
                "Content-Description: ".$file_name."\n" . 
                "Content-Disposition: attachment;\n" . " filename=\"".$file_name."\"; size=".$file_size.";\n" .  
                "Content-Transfer-Encoding: base64\n\n" . $data . "\n\n"; 
            } 
        } 
    } 
     
    $message .= "--{$mime_boundary}--"; 
    $returnpath = "-f" . $senderEmail; 
     
    $mail = @mail($to, $subject, $message, $headers, $returnpath);  
     
    if($mail){ 
        return true; 
    }else{ 
        return false; 
    } 
}

date_default_timezone_set("Asia/Calcutta");
$file1="C:\Python27\working face recg\attendance\\".date('Y-m-d').".xls";
echo $file1;
$f1= fopen("$file1", "r");

date_default_timezone_set("Asia/Calcutta");
$f2=date('Y-m-d').".csv";
$file2 = fopen('$f2','w');
$data=array('Name','Attendance');


$emails=array('1605646@kiit.ac.in','1605618@kiit.ac.in');
$size = count($emails);
echo $size;

for($i =0;$i<$size;$i++)
{
$to = $emails[$i]; 
$from ='<Enter your email>'; 
$fromName = '<Enter your name>'; 
 
$subject = 'Attendance Details';  
 
// Attachment files 
$files = array( 
    $file1 
); 
 
$htmlContent = ' Attendance for date '.date('Y-m-d'); 
 
$sendEmail = multi_attach_mail($to, $subject, $htmlContent, $from, $fromName, $files); 
 
if($sendEmail){ 
    echo 'The email has sent successfully.'; 
}else{ 
    echo 'Mail sending failed!'; 
}
}

?>

