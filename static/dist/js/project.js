var dragAreaVideo = document.querySelector(".video")
var dragImg1 = document.querySelector(".img1")
var dragImg2 = document.querySelector(".img2")
var dragImg3 = document.querySelector(".img3")
var project = document.querySelector(".project")

$(document).ready(function () {

	var current_fs, next_fs, previous_fs; //fieldsets image/png image/jpeg video/mp4
	var opacity;
	var current = 1;
	var countFAQ = 0;
	var data = {
		"projectTitle": "",
		"category": "",
		"subCategory": "",
		"searchTag": [],
		"price": 0,
		"discount": 0,
		"color": "secondary",
		"description": "",
		"FAQ": {},
		"video": "",
		"img1": "",
		"img2": "",
		"img3": "",
		"project": "",
	}

	var steps = $("fieldset").length;

		$(function(){
		$.ajax({
			method: "GET",
			url: "/listcategory",
			success: function (response) {
				// document.querySelector(".lang_level").innerHTML = ""
				var doc = document.querySelector(".category")
				response.map(data => {
					let value = `<option>${data.name}</option>`;
					$(".category").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
		})
	
	$(".category").on("change", (e) => {
		var cat = $(".category").val().trim();
		if (cat) {
			$.ajax({
			method: "GET",
			url: "/listsubcategory",
			data: {"category": cat},
			success: function (response) {
				document.querySelector(".sub-category").innerHTML = `<option value="">SELECT A SUBCATEGORY</option>`
				var doc = document.querySelector(".sub-category")
				response.map(datar => {
					let value = `<option>${datar.name}</option>`;
					$(".sub-category").append(value)
				})
				// document.querySelector(".lang_level").innerHTML = result
			},
			error: function (e) {
				console.log(e)
				return false;
			}
		})
		}
	})

	$(".addBtn-search").click(() => {
		var searchTag = $(".search-tag").val().trim();
		if (searchTag != "" && searchTag != " " && searchTag != "\n") {
			if (data["searchTag"].length <= 4){
			$(".add-search").append(`
			<div class="col-2 border bg-primary text-light text-align rounded-5">${searchTag}</div>
		`);
			data["searchTag"].push(searchTag);
			document.querySelector(".search-tag").value = "";
			}
			if (data["searchTag"].length > 4) {
			Swal.fire(
					'Error',
					"You have reached maximum limit",
					'warning'
			)
			document.querySelector(".search-tag").value = "";
				return false;
		}
			}
	})
	$(".addFAQ").click(() => {
		var question = $(".question").val().trim();
		var answer = $(".answer").val().trim();
		if (question == "" | question == " ") {
			Swal.fire(
					'Error',
					"question can't be empty",
					'warning'
			)
			return false;
			}
		if (answer == "" | answer == " ") {
			Swal.fire(
					'Error',
					"answer can't be empty",
					'warning'
			)
			return false;
		}
		var anon = {}
		anon["question"] = question;
		anon["answer"] = answer;
		data["FAQ"][countFAQ] = anon;
		countFAQ++;
		document.querySelector(".question").value = "";
		document.querySelector(".answer").value = "";
		$(".faq").append(`<div class="accordion-item">
                                            <h4 class="accordion-header" id="headingOne">
                                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                                    data-bs-target="#collapse${countFAQ}" aria-expanded="true"
                                                    aria-controls="collapseOne">${question}
                                                </button>
                                            </h4>
                                            <div id="collapse${countFAQ}" class="accordion-collapse collapse"
                                                aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                                                <div class="accordion-body text-lg-start">${answer}
                                                </div>
                                            </div>
                                        </div>`)
	})
$(".video").click(() => {
	document.querySelector(".videoInput").click()
})
$(".img1").click(() => {
	document.querySelector(".img1Input").click()
})
$(".img2").click(() => {
	if (data["img1"] != ""){
		document.querySelector(".img2Input").click()
	}
	else {
		Swal.fire(
					'Error',
					"Click on the first Image Field",
					'warning'
		)
			return false;
	}
})
$(".img3").click(() => {
	if (data["img1"] != "" & data["img2"] != ""){
		document.querySelector(".img3Input").click()
	}
	else if (data["img1"] == "") {
		Swal.fire(
					'Error',
					"Click on the first Image Field",
					'warning'
		)
			return false;
	}
	else {
		Swal.fire(
					'Error',
					"Click on the second Image Field",
					'warning'
		)
			return false;
	}
})
$(".project").click(() => {
	document.querySelector(".projectInput").click()
})

document.querySelector("body").addEventListener("drop", (e) => {
		e.preventDefault();
})
dragAreaVideo.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragAreaVideo.classList.add("dragError")
  dragAreaVideo.classList.remove("dragSuccess")
	dragAreaVideo.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragAreaVideo.addEventListener("dragleave", (e) => {
  dragAreaVideo.classList.remove("dragError")
  dragAreaVideo.classList.remove("dragHover")
  dragAreaVideo.classList.remove("dragSuccess")
})
document.querySelector(".videoInput").addEventListener("change", (e) =>{
	e.preventDefault();
  dragAreaVideo.classList.remove("dragError")
  dragAreaVideo.classList.remove("dragHover")
	dragAreaVideo.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "video/mp4") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".videoNum").textContent = "(1/1)";
		dragAreaVideo.style.background.url = fileURL;
		data["video"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".videoNum").textContent = "(0/1)";
    dragAreaVideo.classList.add("dragError")
    dragAreaVideo.classList.remove("dragHover")
		dragAreaVideo.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (mp4 format only)",
					'warning'
			)
			return false;
  }
})
	
dragImg1.addEventListener("dragover", (e) => {
	e.preventDefault();
	dragImg1.classList.add("dragError")
  dragImg1.classList.remove("dragSuccess")
	dragImg1.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg1.addEventListener("dragleave", (e) => {
  dragImg1.classList.remove("dragError")
  dragImg1.classList.remove("dragHover")
  dragImg1.classList.remove("dragSuccess")
})
document.querySelector(".img1Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg1.classList.remove("dragError")
  dragImg1.classList.remove("dragHover")
	dragImg1.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "image/png" | folder.type == "image/jpeg") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(1/3)";
		dragImg1.style.background.url = fileURL;
		data["img1"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(1/3)";
    dragImg1.classList.add("dragError")
    dragImg1.classList.remove("dragHover")
		dragImg1.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})
	
dragImg2.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragImg2.classList.add("dragError")
  dragImg2.classList.remove("dragSuccess")
	dragImg2.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg2.addEventListener("dragleave", (e) => {
  dragImg2.classList.remove("dragError")
  dragImg2.classList.remove("dragHover")
  dragImg2.classList.remove("dragSuccess")
})
document.querySelector(".img2Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg2.classList.remove("dragError")
  dragImg2.classList.remove("dragHover")
	dragImg2.classList.add("dragSuccess")
	let folder = e.target.files[0];
	if (folder.type == "image/png" | folder.type == "image/jpeg") {
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(2/3)";
		dragImg2.style.background.url = fileURL;
		data["img2"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(1/3)";
    dragImg2.classList.add("dragError")
    dragImg2.classList.remove("dragHover")
		dragImg2.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})
dragImg3.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragImg3.classList.add("dragError")
  dragImg3.classList.remove("dragSuccess")
	dragImg3.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
dragImg3.addEventListener("dragleave", (e) => {
  dragImg3.classList.remove("dragError")
  dragImg3.classList.remove("dragHover")
  dragImg3.classList.remove("dragSuccess")
})
document.querySelector(".img3Input").addEventListener("change", (e) =>{
  e.preventDefault();
  dragImg3.classList.remove("dragError")
  dragImg3.classList.remove("dragHover")
	dragImg3.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "image/png" | folder.type == "image/jpeg") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".imgNum").textContent = "(3/3)";
		dragImg3.style.background.url = fileURL;
		data["img3"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".imgNum").textContent = "(2/3)";
    dragImg3.classList.add("dragError")
    dragImg3.classList.remove("dragHover")
		dragImg3.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (png/jpeg format only)",
					'warning'
			)
			return false;
  }
})

project.addEventListener("dragover", (e) => {
  e.preventDefault();
  project.classList.add("dragError")
  project.classList.remove("dragSuccess")
	project.classList.remove("dragHover")
	Swal.fire(
					'Error',
					"we don't support drag and drop for now",
					'warning'
			)
			return false;
})
project.addEventListener("dragleave", (e) => {
  project.classList.remove("dragError")
  project.classList.remove("dragHover")
  project.classList.remove("dragSuccess")
})
document.querySelector(".projectInput").addEventListener("change", (e) =>{
  e.preventDefault();
  project.classList.remove("dragError")
  project.classList.remove("dragHover")
  project.classList.add("dragSuccess")
	let folder = e.target.files[0];
  if (folder.type == "application/zip") {
    console.log(folder)
  let fileReader = new FileReader();
  fileReader.onload = ()=>{
    let fileURL = fileReader.result;
    document.querySelector(".projectNum").textContent = "(1/1)";
		project.style.background.url = fileURL;
		data["project"] = folder.name
  };
  fileReader.readAsDataURL(folder);
  }
  else {
		document.querySelector(".projectNum").textContent = "(0/1)";
    project.classList.add("dragError")
  	project.classList.remove("dragHover")
		project.classList.remove("dragSuccess")
		Swal.fire(
					'Error',
					"Unsupported Format (zip format only)",
					'warning'
			)
			return false;
  }
})

	
	$(".next").click(function () {

		current_fs = $(this).parent();
		next_fs = $(this).parent().next();

		if (current == 1) {
			var projectTitle = $(".project-title").val().trim();
			var category = $(".category").val().trim();
			var subCategory = $(".sub-category").val().trim();
			if (projectTitle == "" | projectTitle == " ") {
				Swal.fire(
					'Error',
					"Project title can't be empty",
					'warning'
				)
				return false;
			}
			if (category == "" | category == " ") {
				Swal.fire(
					'Error',
					"category can't be left empty",
					'warning'
				)
				return false;
			}
			if (subCategory == "" | subCategory == " ") {
				Swal.fire(
					'Error',
					"subCategory can't be left empty",
					'warning'
				)
				return false;
			}
			if (data["searchTag"].length <= 0) {
				Swal.fire(
					'Error',
					"Search keyword can't be left empty",
					'warning'
				)
				return false;
			}
			data["projectTitle"] = projectTitle
			data["category"] = category
			data["subCategory"] = subCategory
			console.log(data)
		}
		if (current == 2) {
			var price = $(".price").val().trim();
			var discount = $(".discount").val().trim();
			var color = $(".color").val().trim();
			var lessPrice = parseFloat(price) * 0.07
			if (price == "" | price == " ") {
				Swal.fire(
					'Error',
					"Please select a valid price.",
					'warning'
				)
				return false;
			}
			if (parseFloat(price) == "NaN") {
					Swal.fire(
						'Error',
						"price must be a number",
						'warning'
					)
					return false;
				}
			if (parseFloat(price) < 5) {
					Swal.fire(
						'Error',
						"Minimum price must be $5",
						'warning'
					)
					return false;
				}
			if (discount != "" & discount != " ") {
				if (parseFloat(discount) == "NaN") {
					Swal.fire(
						'Error',
						"discount must be number in percentage format",
						'warning'
					)
					return false;
				}
				if (parseFloat(discount) < 1) {
					Swal.fire(
						'Error',
						"discount can't be less than 1 but must be number in percentage format",
						'warning'
					)
					return false;
				}
				if (parseFloat(discount) < 1) {
					Swal.fire(
						'Error',
						"discount can't be less than 1 but must be number in percentage format",
						'warning'
					)
					return false;
				}
				if (parseFloat(discount) > parseFloat(price)) {
					Swal.fire(
						'Error',
						"discount must not be greater than price",
						'warning'
					)
					return false;
				}
				if (lessPrice > parseFloat(discount)) {
					Swal.fire(
						'Error',
						`Make your pricing calculation well. Failure to do so will lead to low income after NodePair remove ${lessPrice} per income`,
						'warning'
					)
					return false;
				}
				data["discount"] = parseFloat(discount)
			}
			if (color != "") {
				data["color"] = color
			}
			data["price"] = parseFloat(price)
			console.log(data)
		}
		if (current == 3) {
			var description = $(".description").val().trim();
			if (description == "" | description == " ") {
				Swal.fire(
					'Error',
					"description can' be empty.",
					'warning'
				)
				return false;
			}
			data["description"] = description;
			console.log(data)
		}
		if (current == 4) {
			if ((data["img1"] == data["img2"]) & data["img1"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if ((data["img1"] == data["img3"]) & data["img1"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if ((data["img2"] == data["img3"]) & data["img2"] != "") {
				Swal.fire(
					'Error',
					"you can't upload similar images",
					'warning'
				)
				return false;
			}
			if (data["img2"] == "") {
				Swal.fire(
					'Error',
					"you must upload at least two different images",
					'warning'
				)
				return false;
			}
			if (data["project"] == "") {
				Swal.fire(
					'Error',
					"you must upload a project you want to sell.",
					'warning'
				)
				return false;
			}
			document.querySelector(".data").value = JSON.stringify(data);
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
	
});
