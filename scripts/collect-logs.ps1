Write-Output "Collecting Azure activity logs..."

az monitor activity-log list \
--max-events 10 \
--output table
