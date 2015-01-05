var rowNum = 0;
function addRow(frm) {
rowNum ++;

var row = '<p id="rowNum'+rowNum+'"><input type="text" name="qty[]" value="'+frm.add_qty.value+'" placeholder="Name of institution/industry" style="width: 200px;"/> <input type="text" name="name[]" value="'+frm.add_name.value+'" placeholder="Designation" style="width: 170px;"/> <input  type="text"  placeholder="Year: From" name="name[]" style="width: 70px;" /> <input type="text" placeholder="Year: To" name="name[]" style="width: 70px;"/> <input type="button" value="Remove" onclick="removeRow('+rowNum+');"></p>';
roww = '<input type="text" name="add_qty" placeholder="Name of institution/industry" style="width: 200px;" />
                 <input type="text" placeholder="Designation" name="add_name" style="width: 170px;"/>
                 <input  type="text"  placeholder="Year: From" name="add_name" style="width: 70px;" /> 
                 <input type="text" placeholder="Year: To" name="add_name" style="width: 70px;"/>'

jQuery('#itemRows').append(roww);
frm.add_qty.value = '';
frm.add_name.value = '';
}

function removeRow(rnum) {
jQuery('#rowNum'+rnum).remove();
}

