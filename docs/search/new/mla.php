<?php 

if ($_SERVER["REQUEST_METHOD"] == "POST"){
$first_name = $_POST["first_name"];
$last_name = $_POST["last_name"];
$page_title = $_POST["page_title"];
$publisher_title = $_POST["publisher_title"];
$page_title = $_POST["page_title"];
$publication_year = $_POST["publication_year"];
$publication_month = $_POST["publication_month"];
$publication_day = $_POST["publication_day"];
$medium = $_POST["Medium"];
$year_accessed = $_POST["year_accessed"];
$month_accessed = $_POST["month_accessed"];
$day_accessed = $_POST["day_accessed"];

$MLA = "";
$MLA = $MLA . $last_name . ", " . $first_name . ". " .  ' " ' . $page_title . "." .  ' " ' .  '<i>' . 
$publisher_title . '</i>' .  ',' . '  ' . $publication_day . " " .  $publication_month .  " ". $publication_year
 . "." .  " " . $medium . "."  . " " . $day_accessed . " " . $month_accessed . $year_accessed;

echo $MLA;
$MLA =  " ";

}
?>

<DOCTYPE html>
<html>
	<head>
		<title>Harivx Citations</title>
	</head>
	<body>
		<form method="post" action="mla.php">
			 		<table>
			 			<tr>
			 				<th>
								<label for="first_name">First Name</label>
							</th>
							<td>
								<input type="text" name="first_name" id="first_name">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="last_name">Last Name</label>
							</th>
							<td>
								<input type="text" name="last_name" id="last_name">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="page_title">Page Title</label>
							</th>
							<td>
								<input type="text" name="page_title" id="page_title">
							</td>
						</tr>					
						<tr>
			 				<th>
								<label for="publisher_title">Sponsoring Institution / Publisher</label>
							</th>
							<td>
								<input type="text" name="publisher_title" id="publisher_title">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="publication_year">Publication Year</label>
							</th>
							<td>
								<input type="text" name="publication_year" id="publication_year">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="publication_month">Publication Month</label>
							</th>
							<td>
								<select name="publication_month" id="publication_month">
									<option value="January">January</option>
									<option value="Febuary">Febuary</option>
									<option value="March">March</option>
									<option value="April">April</option>
									<option value="May">May</option>
									<option value="June">June</option>
									<option value="July">July</option>
									<option value="August">August</option>
									<option value="September">September</option>
									<option value="October">October</option>
									<option value="November">November</option>
									<option value="December">December</option>
								</select>
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="publication_day">Publication Day</label>
							</th>
							<td>
								<select name="publication_day" id="publication_day">
									<?php 
									$x=1; 
									while($x<=31)
									  {
									  echo '<option value=' . $x . '>' . $x . '</option>';
									  $x++;
									  } 
									?>
								</select>
								
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="medium">Medium</label>
							</th>
							<td>
								<input type="text" name="Medium" id="Medium">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="year_accessed">Year accessed</label>
							</th>
							<td>
								<input type="text" name="year_accessed" id="year_accessed">
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="month_accessed">Month accessed</label>
							</th>
							<td>
								<select name="month_accessed" id="month_accessed">
									<option value="January">January</option>
									<option value="Febuary">Febuary</option>
									<option value="March">March</option>
									<option value="April">April</option>
									<option value="May">May</option>
									<option value="June">June</option>
									<option value="July">July</option>
									<option value="August">August</option>
									<option value="September">September</option>
									<option value="October">October</option>
									<option value="November">November</option>
									<option value="December">December</option>
								</select>
							</td>
						</tr>
						<tr>
			 				<th>
								<label for="day_accessed">Day Accessed</label>
							</th>
							<td>
								<select name="day_accessed" id="day_accessed">
									<?php 
									$x=1; 
									while($x<=31)
									  {
									  echo '<option value=' . $x . '>' . $x . '</option>';
									  $x++;
									  } 
									?>
								</select>
								
							</td>
						</tr>
					</table>
				<input type="submit" value="Send">
		</form>

	</body>
</html>
