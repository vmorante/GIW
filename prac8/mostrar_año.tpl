<h1>{{n}}  usuarios:</h1>
<table>
<tr><th>ID</th><th>e-mail</th></tr>
%for row in c:
	<tr>
	
		 <td>{{row["_id"]}}</td>
         <td>{{row["email"]}}</td>
	
	</tr>
%end
</table>