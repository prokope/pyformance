let data;
let myChart;
let chartIndex = 0;
let chartTitle = document.getElementById('chartTitle');

// Espera o carregamento inicial da DOM
window.addEventListener("DOMContentLoaded", () => {
  // Ativa o fade-in
  document.body.classList.add("fade-in");

  // Aguarda 1s (igual ao tempo do transition), então inicia os gráficos
  setTimeout(() => {
    carregarDadosEExibirGrafico();
  }, 1000);
});

function carregarDadosEExibirGrafico() {
  fetch('./dashboard_summary.json')
    .then(response => response.json())
    .then(jsonData => {
      data = jsonData;
      console.log("Dados carregados:", data);

      chartTitle.textContent = "Top 3 Most Studied Subjects";

      const ctx = document.getElementById('myChart').getContext('2d');
      myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: data.most_studied_subjects,
          datasets: [{
            label: 'Hours Studied',
            data: data.study_time_by_subject,
            backgroundColor: ['#4bc0c0', '#ffcd56', '#36a2eb']
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => console.error("Erro ao carregar o JSON:", error));
}

const ctx = document.getElementById("myChart");

function changeView()
{
    const statistic_option = document.getElementById("statistics").value;
    console.log(statistic_option)
    const span_study_average = document.getElementById('study_average')

    if (statistic_option == "exercises_performance")
    {
        // Show the second summary statistics (Update chart)
        ctx.style.display = "flex";
        span_study_average.style.display = "none";
        myChart.config.type = 'pie'

        
        myChart.data.labels = ["Correct Answers", "Wrong Answers"];
        myChart.data.datasets[0].data = [data.percentage_correct_answers, data.percentage_wrong_answers];
        myChart.data.datasets[0].backgroundColor = ['#4CAF50', '#F44336'];
        myChart.data.datasets[0].label = "Percentage"
        myChart.update();

        chartTitle.textContent = "Exercises Performance"
    }

    else if (statistic_option == "average_study_time")
    {
        // Show the third summary statistics (Update chart)
        ctx.style.display = "none";
        span_study_average.style.display = "block";
        chartTitle.textContent = "Daily Study Average"
        span_study_average.textContent = `${data.average_daily_study} Hours`;
        chartIndex = 0;
    }

    else if (statistic_option == "most_studied_subjects")
    {
        // Show the first summary statistics (Update chart)
        ctx.style.display = "flex";
        chartIndex = 0
    }
}