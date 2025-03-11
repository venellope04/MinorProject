const APP_ID = '71fbf1e2263a49869725faa8404523ec';
let client = AgoraRTC.createClient({ mode: "rtc", codec: "vp8" });
let localTracks = [];
let remoteUsers = {};

const joinBtn = document.getElementById('joinBtn');
const leaveBtn = document.getElementById('leaveBtn');
const videoContainer = document.getElementById('video_container');

// Function to stop all local tracks
const stopLocalTracks = () => {
    localTracks.forEach(track => track.stop());
    localTracks = [];
};

// Join Room Logic
joinBtn.onclick = async () => {
    try {
        const response = await fetch(`/get_token/?channelName=${roomName}`);
        const data = await response.json();

        await client.join(APP_ID, roomName, data.token, data.uid);

        // Stop any existing local tracks before creating new ones
        stopLocalTracks();

        // Create a container for the local video
        const localPlayer = document.createElement("div");
        localPlayer.id = `user-${data.uid}`;
        localPlayer.style.width = "400px";
        localPlayer.style.height = "300px";
        videoContainer.appendChild(localPlayer);

        // Display Local Video
        const localTrack = await AgoraRTC.createCameraVideoTrack();
        localTracks.push(localTrack);
        localTrack.play(localPlayer);

        joinBtn.disabled = true;
        leaveBtn.disabled = false;

        // Handle Remote Users
        client.on("user-published", async (user, mediaType) => {
            await client.subscribe(user, mediaType);
            if (mediaType === "video") {
                const remotePlayer = document.createElement("div");
                remotePlayer.id = `user-${user.uid}`;
                remotePlayer.style.width = "400px";
                remotePlayer.style.height = "300px";
                videoContainer.appendChild(remotePlayer);
                user.videoTrack.play(remotePlayer);
                remoteUsers[user.uid] = user;
            }
        });

        client.on("user-unpublished", user => {
            const remotePlayer = document.getElementById(`user-${user.uid}`);
            if (remotePlayer) remotePlayer.remove();
            delete remoteUsers[user.uid];
        });

    } catch (err) {
        console.error("Failed to join room:", err);
    }
};

// Leave Room Logic
leaveBtn.onclick = async () => {
    stopLocalTracks();
    await client.leave();
    document.getElementById('video_container').innerHTML = '';
    Object.values(remoteUsers).forEach(user => {
        const remotePlayer = document.getElementById(`user-${user.uid}`);
        if (remotePlayer) remotePlayer.remove();
    });
    remoteUsers = {};

    joinBtn.disabled = false;
    leaveBtn.disabled = true;
};
