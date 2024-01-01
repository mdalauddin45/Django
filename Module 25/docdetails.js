const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    loadTime(param);
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
      .then((res) => res.json())
      .then((data) => displayDetails(data));
  
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
      .then((res) => res.json())
      .then((data) => doctorReview(data));
  };
  