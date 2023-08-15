select profile.member_name, review.review_text, date_format(review.review_date, "%Y-%m-%d")
from member_profile profile
    join rest_review review
    on review.member_id = member.member_id
where profile.member_id = (select member_id from rest_review
group by member_id
order by count(*) desc
limit 1
)
order by review.review_date , review.review_text