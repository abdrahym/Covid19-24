SELECT 
    location,
    strftime('%Y', date) AS Year,
    strftime('%m', date) AS Month,
    strftime('%Y', date) || '-' || strftime('%m', date) AS YearMonth,
    SUM(total_cases) AS TotalCases,
    SUM(total_deaths) AS TotalDeaths,
    ROUND((SUM(total_deaths) / SUM(total_cases)) * 100, 2) AS DeathPercentage,
    ROUND((SUM(total_cases) / MAX(population)) * 100, 2) AS CasePopulationPercentage,
    ROUND((SUM(total_deaths) / MAX(population)) * 100, 2) AS DeathPopulationPercentage,
    MAX(population) AS population
FROM covidDeaths
GROUP BY location, strftime('%Y', date), strftime('%m', date)
ORDER BY 3 ASC, 2 ASC, 1 ASC
