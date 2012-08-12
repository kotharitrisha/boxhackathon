
project_id = 0
$(document).ready(function(){ 	
    console.log("I am up");  
    
	addTask = function(data){
		$("#new-project-dialog").dialog("close");
		console.log("Add Task");
		var width = $(window).width();
		var height = $(window).height();

		// Provide some space between the window edges.
		var width = width - 100;
		var height = height - 100;
		var title = 'Add Task';	
		$("#new-task-dialog").data = data
		$("#new-task-dialog").dialog({ title: title, height: height, width: width, autoOpen:false, modal: true});		
		$("#new-task-dialog").dialog("open");
		console.log("pro_id " + project_id)
	}




	addMoreTask = function(){	
		console.log("Add More Task"); 
		$("#new-task-dialog").dialog("open");
	}

	doneAllTasks = function(){
		$("#new-task-dialog").dialog("close");
	} 
    
    projects_table = $('#projects-table').dataTable({
		"sDom": '<"top"f<"clear">>rt<"bottom"ilp<"clear">>',
        "bPaginate": false,
        "bInfo": false,
        "bAutoWidth": false,
        "bFilter": false,
        "sWidth": "100%",
        "aoColumns": [			
        	{"bSortable": false, "sWidth": "100%"}
        ]
    
    });
    
    
    tasks_table = $('#tasks-table').dataTable({
		"sDom": '<"top"f<"clear">>rt<"bottom"ilp<"clear">>',
        "bPaginate": false,
        "bInfo": false,
        "bAutoWidth": false,
        "bFilter": false,
        "sWidth": "100%",
        "aoColumns": [			
        	{"bSortable": false, "sWidth": "20%"},
        	{"bSortable": false, "sWidth": "60%"},
        	{"bSortable": false, "sWidth": "20%"}
        ]
    
    });
    
    get_projects = function(params) {
		
		
		var jaqxhr = $.post("/ajax/project_search/",
			{},
			function(data){
				projects_table.fnClearTable();
				populate_projects_table(data);
			}); 			
			
	}
	
	
	get_tasks = function(id) {
		console.log("getting tasks");
		var jaqxhr = $.post("/ajax/task_search/",
			{'id':id},
			function(data){
				tasks_table.fnClearTable();
				populate_tasks_table(data);
			}); 
			
			
	}
	
	
	add_task = function(data) {
		console.log("add tasks");
		console.log("pro_id " + project_id)
		params = {};
		params.desc = $("#task_desc").val();
		params.owner = $("#task_owner").val();
		params.deadline = $("#task_deadline").val();
		params.project_id = project_id
		console.log(params);
		console.log("added task");		
		var jaqxhr = $.post("/ajax/task_add/",
			{'desc': params.desc,
			'owner': params.owner,
			'deadline': params.deadline,
			'project_id': params.project_id},			
			function(data){
				addMoreTask(data);
			}); 
			
			
	}
	
	add_project = function() {
		console.log("here");
		params = {};
		params.title = $("#project_title").val();
		params.desc = $("#project_desc").val();
		params.filename = $("#project_filename").val();
		console.log("params " +  params.toString());		
		var jaqxhr = $.post("/ajax/project_add/",
			{'title': params.title,
			'desc': params.desc,
			'filename': params.filename},
			function(data){
				console.log(data)
				x = JSON.parse(data)
				project_id = x.id
				console.log('orig id')
				console.log(project_id)
				addTask(data);
			}); 
			
			
	}
	
	
	function bind(fnc, val ) {
		return function () {
			return fnc(val);
		};
	}
	
	function populate_projects_table(data){
		var x = JSON.parse(data)
		console.log(x)
		for(var i = 0; i< x.projects.length; i++){
			curr = projects_table.fnAddData( [
								x.projects[i].title
							  ]);	
			var id = x.projects[i].id	
			var f = bind(get_tasks, id)		  
			curr_row = projects_table.fnGetNodes(curr);
			$(curr_row).click(f);
		}
		
	}
	
	
	function populate_tasks_table(data){
		console.log("Inside Populate Tasks");
		var x = JSON.parse(data)
		console.log(x)
		for(var i = 0; i< x.tasks.length; i++){
		curr = tasks_table.fnAddData( [
       						x.tasks[i].desc,
       						x.tasks[i].owner_id,
       						x.tasks[i].step_deadline
		                  ]);					
		}	
	}
	
	new_project = function() {
		var width = $(window).width();
		var height = $(window).height();

		// Provide some space between the window edges.
		var width = width - 100;
		var height = height - 100;
		var title = 'New Project';
		$('#new-project-dialog').dialog({ title: title, height: height, width: width });
			
	}

	$('#new-project-link').click(new_project);
	get_projects();
	
});
