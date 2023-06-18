input = document.querySelector(".pics")
$(".picer").hide();

$(document).ready(function () {

	var token = document.querySelector("input[name=csrfmiddlewaretoken]");
	var user = $(".u_token").val();
	var current_fs, next_fs, previous_fs; //fieldsets
	var opacity;
	var current = 1;
	var count = 0;
	var counts = 0;
	var countl = 0;
	var successfulSubmit = false;
	let pics;
	var res = true;
	var steps = $("fieldset").length;
	var data = {
		"fullname": "",
		"slogan": "",
		"profile_pics": "",
		"description": "",
		"language": {},
		"occupation":{},
		"skills": {},
		"url": "",
	}
	$(".picer").hide();

	setProgressBar(current);
function validate_year(fyear, tyear){
	if (isNaN(fyear) | isNaN(tyear)){
		Swal.fire(
			'Error',
			 "please confirm that the year is in right format",
			 'warning'
		)
		return false;
	}
	if ( fyear.toString().length != 4 | tyear.toString().length != 4) {
		Swal.fire(
			'Error',
			 "please confirm that the year is in right format",
			 'warning'
		)
		return false;
	}
	if (!fyear.length | !tyear.length){
		Swal.fire(
			'Error',
			 "please confirm that the year fields is not empty",
			 'warning'
		)
		return false;
	}
	if (parseInt(fyear) > parseInt(tyear)) {
		Swal.fire(
			'Error',
			 "starting year can't be greater than ending yaer",
			 'warning'
		)
		return false;
	}
	return true;
}
$(function(){
		$.ajax({
			method: "GET",
			url: "/listLanguage",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".lang_level")
				response.map(data => {
					let value = `<option>${data.language}</option>`;
					$(".lang_level").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
	})
$(function(){
		$.ajax({
			method: "GET",
			url: "/listOccupation",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".occup")
				response.map(data => {
					let value = `<option>${data.occupations}</option>`;
					$(".occup").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
	})
$(function(){
		$.ajax({
			method: "GET",
			url: "/listSkill",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".skill")
				response.map(data => {
					let value = `<option>${data.skiller}</option>`;
					$(".skill").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
	})

$(function(){
		$.ajax({
			method: "GET",
			url: "/listSkillLevel",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".level")
				response.map(data => {
					let value = `<option>${data.skill_level}</option>`;
					$(".level").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
	})

	$(".pic").click(function () {
		$(".pics").click();
	});

	$(".picer").click(function () {
		$(".pics").click();
	});

	input.addEventListener("change", function (){
		let folder = this.files[0];
		if (folder.type == "image/png" | folder.type == "image/jpeg") {
		let fileReader = new FileReader();
		fileReader.onload = ()=>{
		  let fileURL = fileReader.result;
		  pics = fileURL
		  pict = document.querySelector(".picer")
		  pict.src = fileURL
		  
		  $(".pic").hide();
		  $(".picer").show();
		};
		fileReader.readAsDataURL(folder);
		}
	})

	$(".langs").click(function () {
		var language = {};

		var lang = $(".lang").val();
		var level = $(".lang_level").val();
		if (lang=="" | lang ==" "){
			Swal.fire(
				'Error',
				 "language name must not be empty",
				 'warning'
			)
		}
		else if (level=="" | level ==" "){
			Swal.fire(
				'Error',
				 "your language level must not be empty",
				 'warning'
			)
		}
		else{
			language["name"] = lang;
			language["level"] = level;
			
			$(".langer").append(`<div class="row">
			<div class="col-4">
			</div>
			<div class="col-4 border">
				<h6 class="text-light bg-primary w-100 p-0">${lang}</h6>
			</div>
			<div class="col-4 border">
				<h6 class="text-light bg-secondary w-100 p-0">${level}</h6>
			</div>
		</div>`)
			
			data["language"][countl] = language
			countl = countl + 1;
			$(".lang").val("")
			console.log(data)

		}
	});
	$(".addo").click(function () {
		var occupation = {};

		var occup = $(".occup").val();
		var fyear = $(".fyear").val();
		var tyear = $(".tyear").val();
		if (occup=="" | occup ==" "){
			Swal.fire(
				'Error',
				 "occupation name must not be empty",
				 'warning'
			)
		}
		else if (fyear=="" | fyear ==" "){
			Swal.fire(
				'Error',
				 "year must not be empty",
				 'warning'
			)
		}
		else if (tyear=="" | tyear ==" "){
			Swal.fire(
				'Error',
				 "year must not be empty",
				 'warning'
			)
		}
		else if(validate_year(fyear, tyear)){
			occupation["occup"] = occup;
			occupation["fyear"] = fyear;
			occupation["tyear"] = tyear;
			
			$(".occupv").append(`<div class="row">
			<div class="col-3">
			</div>
			<div class="col-3 border">
				<h6 class="text-light bg-primary w-100 p-0">${occup}</h6>
			</div>
			<div class="col-3 border">
				<h6 class="text-light bg-secondary w-100 p-0">${fyear}</h6>
			</div>
			<div class="col-3 border">
				<h6 class="text-light bg-secondary w-100 p-0">${tyear}</h6>
			</div>
			</div>`)
			
			data["occupation"][count] = occupation
			count = count + 1;
		}
	});

	$(".addsk").click(function () {
		var skills = {};

		var skill = $(".skill").val();
		var level = $(".level").val();

		if (skill=="" | skill ==" "){
			Swal.fire(
				'Error',
				 "skills must not be empty",
				 'warning'
			)
		}
		else if (level=="" | level ==" "){
			Swal.fire(
				'Error',
				 "levels must not be empty",
				 'warning'
			)
		}
		else{
			skills["skill"] = skill;
			skills["level"] = level;
			
			$(".occups").append(`<div class="row">
			<div class="col-4">
			</div>
			<div class="col-4 border">
				<h6 class="text-light bg-primary w-100 p-0">${skill}</h6>
			</div>
			<div class="col-4 border">
				<h6 class="text-light bg-secondary w-100 p-0">${level}</h6>
			</div>
		</div>`)
		
		data["skills"][counts] = skills
		counts = counts + 1;
			}
	});

	$(".next").click(async function () {

		current_fs = $(this).parent();
		next_fs = $(this).parent().next();

		if (current == 1){
			var fullname = $(".fullname").val();
			var slogan = $(".slogan").val();
			var desc = $(".desc").val();
			if (fullname == "" | fullname == " "){
				Swal.fire(
					'Error',
					 "Fullname is required",
					 'warning'
				)
				return false;
			}
			else if (slogan == "" | slogan == " "){
				Swal.fire(
					'Error',
					 "slogan must not be left empty",
					 'warning'
				)
				return false;
			}

			else if (desc == "" | desc == " "){
				Swal.fire(
					'Error',
					 "description must not be left empty",
					 'warning'
				)
				return false;
			}
			else if (pics == "" | pics == null){
				Swal.fire(
					'Error',
					 "It is strongly advicable to add a profile picture of yourself",
					 'warning'
				)
				return false;
			}
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
					if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
					}
				}
				})
				
				if (confirmText != "nodepair") {
				return false;
				}
			

			data["fullname"] = fullname;
			data["slogan"] = slogan;
			data["profile_pics"] = pics;
			data["description"] = desc;
			console.log(data)

		}

		if (current == 2){
			var url = $(".url").val();
			const { value: confirmText } = await Swal.fire({
				title: 'Are you sure?',
				text: "You won't be able to go back!",
				input: 'text',
				inputLabel: 'type nodepair',
				showCancelButton: true,
				allowOutsideClick: false,
				inputValidator: (value) => {
				  if (!value | value != "nodepair") {
					return 'You need to write nodepair in the input field!'
				  }
				}
			  })
			  
			  if (confirmText != "nodepair") {
				return false;
			  }
			data["url"] = url;
			$.ajax({
				async: false,
				method: "POST",
				url: "/soap",
				data: {
				  'info': data,
				  'occup': count,
				  'skill': counts,
				  'language': countl,
				  csrfmiddlewaretoken: token.value,
				},
				// datatype: "dataType",
				success: function (response) {
					successfulSubmit = true
					Swal.fire(
						'Success!!!',
						response.status,
						'success'
				   )
				},
				error: function (e) {
					successfulSubmit = false
					Swal.fire({
						icon: 'error',
						title: 'Oops...',
						allowOutsideClick: false,
						text: `Something went wrong!`,
						footer: '<a href="">Why do I have this issue?</a>'
					  })
					return false;
				}
			})
			if (successfulSubmit == false){
				return false;
			}
		}
		//Add Class Active
		$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

		//show the next fieldset
		next_fs.show();
		//hide the current fieldset with style
		current_fs.animate({ opacity: 0 }, {
			step: function (now) {
				// for making fielset appear animation
				opacity = 1 - now;

				current_fs.css({
					'display': 'none',
					'position': 'relative'
				});
				next_fs.css({ 'opacity': opacity });
			},
			duration: 500
		});
		setProgressBar(++current);
	});

	function setProgressBar(curStep) {
		var percent = parseFloat(100 / steps) * curStep;
		percent = percent.toFixed();
		$(".progress-bar")
			.css("width", percent + "%")
	}

	$(".submit").click(function () {
		return false;
	})
	
});
