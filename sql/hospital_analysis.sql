-- Hospital Performance & Quality Analytics
-- Import the CMS CSV into a table named hospitals before running these queries.
-- Keep facility_id as TEXT.

-- 1. Total number of hospitals
SELECT COUNT(*) AS total_hospitals
FROM hospitals;

-- 2. Hospitals by state
SELECT state, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY state
ORDER BY hospital_count DESC;

-- 3. Hospitals by type
SELECT hospital_type, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY hospital_type
ORDER BY hospital_count DESC;

-- 4. Hospitals by ownership
SELECT hospital_ownership, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY hospital_ownership
ORDER BY hospital_count DESC;

-- 5. Overall rating distribution
SELECT hospital_overall_rating, COUNT(*) AS hospital_count
FROM hospitals
WHERE hospital_overall_rating IS NOT NULL
GROUP BY hospital_overall_rating
ORDER BY hospital_overall_rating;

-- 6. Hospitals offering emergency services
SELECT emergency_services, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY emergency_services
ORDER BY hospital_count DESC;

-- 7. Hospitals without an overall rating
SELECT COUNT(*) AS hospitals_without_rating
FROM hospitals
WHERE hospital_overall_rating IS NULL
   OR TRIM(CAST(hospital_overall_rating AS TEXT)) = '';

-- 8. Check duplicate hospital IDs
SELECT facility_id, COUNT(*) AS id_count
FROM hospitals
GROUP BY facility_id
HAVING COUNT(*) > 1;

-- 9. Hospital count by state and ownership
SELECT state, hospital_ownership, COUNT(*) AS hospital_count
FROM hospitals
GROUP BY state, hospital_ownership
ORDER BY state, hospital_count DESC;
