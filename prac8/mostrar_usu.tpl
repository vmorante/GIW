
<tr>
	<th>row["_id"]</th>
	<th>row["email"]</th>
	<th>row["password"]</th>
	<th>row["gender"]</th>
	<th>row["address"]["country"]</th>
	<th>row["address"]["zip"]</th>
	<th>row["year"]</th>
	%for col in row["likes"]:
		<td>{{col}},</td>
	%end
</tr>

