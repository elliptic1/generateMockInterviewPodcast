import eyed3

from util import get_article


def add_metadata(company, job_post_title, interviewee_voice, interviewee_old_job_title, interviewee_old_company):

    audiofile = eyed3.load("output/final.mp3")
    audiofile.initTag()

    audiofile.tag.artist = "Tech Star Podcast"
    audiofile.tag.album = "Mock Interviews in the Tech Industry"
    audiofile.tag.album_artist = f"{interviewee_voice}, {get_article(interviewee_old_job_title)} {interviewee_old_job_title} at {interviewee_old_company}"
    audiofile.tag.title = f"{job_post_title} Interview with {company}"
    audiofile.tag.track_num = 1

    audiofile.tag.save()
