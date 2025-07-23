import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 50)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the duration of the video: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print(f"Video '{name}' added successfully.")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new duration of the video: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print(f"Video '{name}' updated successfully.")
    else:
        print("Invalid index.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print(f"Video deleted successfully.")
    else:
        print("Invalid index.")

def main():
    videos = load_data()
    
    while True:
        print("\nYouTube Video Manager")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()