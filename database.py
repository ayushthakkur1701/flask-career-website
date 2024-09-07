from dotenv import load_dotenv

load_dotenv()
import os
from supabase import create_client


url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase= create_client(url, key)


def get_all_jobs():
  jobitems =supabase.table("jobs").select("*").execute()
  jobitems_dict = []

  for jobitem in jobitems.data:
      jobitems_dict.append(jobitem)  

  return jobitems_dict
  
  

