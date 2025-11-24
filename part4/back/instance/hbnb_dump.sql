PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO users VALUES('406d6b13-bdf0-450d-8101-5e793eaac584','Admin','HBnB','admin@hbnb.io','$2b$12$Etdci8aRYvh4oOZdY7igOOCUf2Sk.v86A5N5RIZgTFIPdH1FJjg9K',1,'2025-11-17 15:18:18.383484','2025-11-17 15:18:18.383514');
INSERT INTO users VALUES('45108a38-e3ea-4863-b6e5-896bdbcc0cc2','User','HBnB','user@hbnb.io','$2b$12$THtYuBEuMefNuj76530tDu/FEKq9iTfYx3mlpFoA808YlsFWIbno2',0,'2025-11-17 15:54:41.263396','2025-11-17 15:54:41.263409');
INSERT INTO users VALUES('11d61199-5215-457a-919e-595f8eb819a3','Thierry','Sensualite','titidu29@breizh.com','$2b$12$Ggoyf2bi.ULPszgXJisQpeowmM04yeSarf5ENrOCoHuRbCgZ9LAMq',0,'2025-11-18 13:14:18.945794','2025-11-18 13:14:18.945803');
INSERT INTO users VALUES('29f9fcd6-fd2a-4118-ba84-c3b443ba770e','Thierry','Sensualité','titidulove@hbnb.io','$2b$12$lpNjFKCslU6YPI61o7KDwe1DqNXWQD50aVJyv9SeIpTG/Yx3eQCju',0,'2025-11-20 12:40:43.694726','2025-11-20 12:40:43.694734');
INSERT INTO users VALUES('7e1554ad-bf66-4460-8126-74ccaaa862e2','Baron','Von Porcelain','creeplord@hbnb.io','$2b$12$0dex4heewb9WJ2JBEqpQZeJRX7pxziQ7oGCztB6UEXHoxRSwAw4wK',0,'2025-11-20 12:42:00.248114','2025-11-20 12:42:00.248118');
INSERT INTO users VALUES('26198b75-979e-4b74-86e1-41e6f52ed3cf','Marc et Virgine','Lovebirds','love4ever@hbnb.io','$2b$12$JMcxJPnlSH0kvF/ZYsnOEOdmW7D5Nk27nPpo44YO1BlxqlS2oouFe',0,'2025-11-20 12:42:32.142354','2025-11-20 12:42:32.142357');
INSERT INTO users VALUES('3d32397a-b3a3-4c0e-bad9-c4df1eaced21','Marc et Virginie','Lovebirds','loverz4ever@hbnb.io','$2b$12$8hnynOAn0SYH4h/sNSSC2esHULptpc3ydTr7OTpD.HMXsweabIO/6',0,'2025-11-20 12:42:55.727325','2025-11-20 12:42:55.727329');
INSERT INTO users VALUES('595d7df7-c3ea-46ad-ab0f-8dbfdf660db3','Sandrine','Depreschön','IloveLife@hbnb.io','$2b$12$UoMY9z7Wdj7qCLHPorPcKOq1VWSj9gIViMZO6gNrLiPDoBPLHHtAy',0,'2025-11-20 12:44:04.895234','2025-11-20 12:44:04.895238');
INSERT INTO users VALUES('7efb9716-088c-41c2-9e9f-a80873c4d7d6','Annabelle','x.x','anna_belle@hbnb.io','$2b$12$HDz20fr/a5mF78Pc4ZAehukCo/S3hTIN7px5fZfrWK7PenMv1Mjgi',0,'2025-11-20 15:56:00.938073','2025-11-20 15:56:00.938080');
INSERT INTO users VALUES('f3ce8032-be48-4d5f-9aaa-37b8211afb5e','Shaggy','Rogers','scooby_gang@hbnb.io','$2b$12$0GgpxJRqY7spC1y/ew.6ReRF6Y7zUCUjHeHhb0m0CGaX//Pagrs6i',0,'2025-11-20 15:58:13.900108','2025-11-20 15:58:13.900112');
INSERT INTO users VALUES('a1d2cd17-0e08-4852-be15-56c2d64d7ebf','Donald','Trump','bigboy@hbnb.io','$2b$12$gA/CtycA1Q5FJqpBUfuX9OAaG2u4UDIv8.JyVd2cbhEh1b47m6aBe',0,'2025-11-20 15:59:11.447919','2025-11-20 15:59:11.447923');
INSERT INTO users VALUES('bae50443-df15-4f49-acec-aa212f5ace82','Sheldon','Cooper','physics@hbnb.io','$2b$12$EOrr2gHrn1ufnURtCjqA9eB5A./1ma17cUjPvqi.vli0GPNQDXTIW',0,'2025-11-20 16:01:56.108706','2025-11-20 16:01:56.108710');
INSERT INTO users VALUES('f1c27fa6-fe3e-44f5-b2b9-6899540dfa2d','Dwight','Schrute','farming4life@hbnb.io','$2b$12$U4lUi87kvaXqfDu0MvVJluhPmQ.N.bm5zmTxK/UhXAk1Y8tSHXaRi',0,'2025-11-20 16:03:19.274958','2025-11-20 16:03:19.274964');
CREATE TABLE amenities (
    id TEXT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO amenities VALUES('666ab72a-9b59-477b-8fc8-690559508963','Haunted dolls','2025-11-20 12:46:17.530702','2025-11-20 12:46:17.530705');
INSERT INTO amenities VALUES('b5365c10-6b47-4b21-90dd-1d2eded0847b','Flickering lights','2025-11-20 12:47:35.648875','2025-11-20 12:47:35.648879');
INSERT INTO amenities VALUES('7317b197-efb3-406a-b52c-e26b3e10bb35','Shadowy corners','2025-11-20 12:47:45.228050','2025-11-20 12:47:45.228053');
INSERT INTO amenities VALUES('539bf07b-5d6e-45d4-9b43-855c1ccb83b5','Constant whispers','2025-11-20 12:47:58.623496','2025-11-20 12:47:58.623499');
INSERT INTO amenities VALUES('9f7abf37-9014-4afc-b5c1-3a9502320de0','Non-stop PDA','2025-11-20 12:48:42.741682','2025-11-20 12:48:42.741686');
INSERT INTO amenities VALUES('ec558687-a59e-48c8-813e-7149c09f17e7','Live Love Laugh','2025-11-20 12:50:40.573851','2025-11-20 12:50:40.573858');
INSERT INTO amenities VALUES('4c04d256-03a6-4869-a62d-54820440e0bc','Nice pics of us','2025-11-20 12:51:00.103111','2025-11-20 12:51:00.103115');
INSERT INTO amenities VALUES('664e4fb5-f092-4458-975c-d00f76256045','Endless tenderness','2025-11-20 12:51:13.600096','2025-11-20 12:51:13.600099');
INSERT INTO amenities VALUES('0560fab7-60a3-4bf0-9771-cefc2d63f252','Xanax','2025-11-20 12:51:27.302815','2025-11-20 12:51:27.302819');
INSERT INTO amenities VALUES('80d32931-ecfe-4267-a45d-127c7d6ca05d','Prozac','2025-11-20 12:51:35.963975','2025-11-20 12:51:35.963980');
INSERT INTO amenities VALUES('51f26f5d-04f2-4941-9825-90f546649c3b','Melancholy','2025-11-20 12:51:48.127057','2025-11-20 12:51:48.127127');
INSERT INTO amenities VALUES('8cdd97dc-fdfe-4890-94e3-227d38ab9c53','Endless suffering','2025-11-20 12:51:58.716409','2025-11-20 12:51:58.716413');
INSERT INTO amenities VALUES('779135a9-2d6d-4b7d-9947-72753d097204','Massages','2025-11-20 12:52:18.750609','2025-11-20 12:52:18.750614');
INSERT INTO amenities VALUES('5e089331-6f71-4d1a-bd92-85d88f65aecd','Epanouissement personnel','2025-11-20 12:52:35.249314','2025-11-20 12:52:35.249318');
INSERT INTO amenities VALUES('b5a755af-e094-4d05-894d-c3d152dc464b','Eveil des sens','2025-11-20 12:52:47.702134','2025-11-20 12:52:47.702137');
INSERT INTO amenities VALUES('604b4fd7-077a-4a54-a421-c7d1c76b5f69','Jacuzzi','2025-11-20 12:52:59.597543','2025-11-20 12:52:59.597547');
INSERT INTO amenities VALUES('071fcf3a-1782-4c1b-9412-6b7c8bc3fd91','Champagne','2025-11-20 12:53:12.530591','2025-11-20 12:53:12.530595');
CREATE TABLE reviews (
    id TEXT PRIMARY KEY,
    text VARCHAR(5000) NOT NULL,
    rating INTEGER NOT NULL,
    place_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
INSERT INTO reviews VALUES('94cbea40-ffdf-4144-a3a1-e77bccd34616','mouahahaha',1,'02816bc6-0d8d-4400-9704-0163aa22aadd','11d61199-5215-457a-919e-595f8eb819a3','2025-11-19 14:58:14.390191','2025-11-19 14:58:14.390195');
INSERT INTO reviews VALUES('ecbc84a1-7baa-4711-81c5-dd4671f9269d','Great place, I felt right at home.',5,'bd5fd617-140a-4475-96f3-6d4ff0b64c0c','7efb9716-088c-41c2-9e9f-a80873c4d7d6','2025-11-23 16:11:41.383305','2025-11-23 16:11:41.383312');
INSERT INTO reviews VALUES('4eb99b47-407f-4106-86b4-fb21039cab9b','The place is like quite noisy at home, I didn''t get mush sleep. The food was good tho, and like they accepted my dog in the room so like, ok.',2,'bd5fd617-140a-4475-96f3-6d4ff0b64c0c','f3ce8032-be48-4d5f-9aaa-37b8211afb5e','2025-11-23 16:20:52.857742','2025-11-23 16:20:52.857745');
INSERT INTO reviews VALUES('925d7875-219a-4847-949e-375c53cfae95','Best night ever.',5,'6a9faaf8-04c9-4110-9626-8ff97001c84b','a1d2cd17-0e08-4852-be15-56c2d64d7ebf','2025-11-23 16:22:32.355904','2025-11-23 16:22:32.355909');
INSERT INTO reviews VALUES('7990eafe-89b4-4b2d-865f-192a0120dbe2','Charming place. During my stay, the host experienced a critical safety incident due to poor situational awareness. Fortunately, I responded with the speed and precision of a seasoned volunteer sheriff’s deputy. Crisis neutralized. Another day in which my superior reflexes preserved life and order.',4,'0d9e335c-2c8d-48c2-87d4-a2ca977cd733','f1c27fa6-fe3e-44f5-b2b9-6899540dfa2d','2025-11-23 16:27:37.882885','2025-11-23 16:27:37.882890');
INSERT INTO reviews VALUES('235b76ce-bf70-4ee6-b433-41681a17ba81','There was no Wi-Fi, despite the explicit assertion in the listing’s title. Highly disappointing, and frankly a violation of basic expectations for civilized habitation.',1,'0d9e335c-2c8d-48c2-87d4-a2ca977cd733','bae50443-df15-4f49-acec-aa212f5ace82','2025-11-23 16:30:26.782216','2025-11-23 16:30:26.782220');
CREATE TABLE place_amenity (
    place_id TEXT NOT NULL,
    amenity_id TEXT NOT NULL,
    PRIMARY KEY(place_id, amenity_id),
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(amenity_id) REFERENCES amenities(id)
);
INSERT INTO place_amenity VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','071fcf3a-1782-4c1b-9412-6b7c8bc3fd91');
INSERT INTO place_amenity VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','604b4fd7-077a-4a54-a421-c7d1c76b5f69');
INSERT INTO place_amenity VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','b5a755af-e094-4d05-894d-c3d152dc464b');
INSERT INTO place_amenity VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','779135a9-2d6d-4b7d-9947-72753d097204');
INSERT INTO place_amenity VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','5e089331-6f71-4d1a-bd92-85d88f65aecd');
INSERT INTO place_amenity VALUES('0d9e335c-2c8d-48c2-87d4-a2ca977cd733','0560fab7-60a3-4bf0-9771-cefc2d63f252');
INSERT INTO place_amenity VALUES('0d9e335c-2c8d-48c2-87d4-a2ca977cd733','80d32931-ecfe-4267-a45d-127c7d6ca05d');
INSERT INTO place_amenity VALUES('0d9e335c-2c8d-48c2-87d4-a2ca977cd733','51f26f5d-04f2-4941-9825-90f546649c3b');
INSERT INTO place_amenity VALUES('0d9e335c-2c8d-48c2-87d4-a2ca977cd733','8cdd97dc-fdfe-4890-94e3-227d38ab9c53');
INSERT INTO place_amenity VALUES('ce42aca7-a740-43c9-9eda-c9381bb35b03','9f7abf37-9014-4afc-b5c1-3a9502320de0');
INSERT INTO place_amenity VALUES('ce42aca7-a740-43c9-9eda-c9381bb35b03','ec558687-a59e-48c8-813e-7149c09f17e7');
INSERT INTO place_amenity VALUES('ce42aca7-a740-43c9-9eda-c9381bb35b03','4c04d256-03a6-4869-a62d-54820440e0bc');
INSERT INTO place_amenity VALUES('ce42aca7-a740-43c9-9eda-c9381bb35b03','664e4fb5-f092-4458-975c-d00f76256045');
INSERT INTO place_amenity VALUES('bd5fd617-140a-4475-96f3-6d4ff0b64c0c','666ab72a-9b59-477b-8fc8-690559508963');
INSERT INTO place_amenity VALUES('bd5fd617-140a-4475-96f3-6d4ff0b64c0c','b5365c10-6b47-4b21-90dd-1d2eded0847b');
INSERT INTO place_amenity VALUES('bd5fd617-140a-4475-96f3-6d4ff0b64c0c','7317b197-efb3-406a-b52c-e26b3e10bb35');
INSERT INTO place_amenity VALUES('bd5fd617-140a-4475-96f3-6d4ff0b64c0c','539bf07b-5d6e-45d4-9b43-855c1ccb83b5');
CREATE TABLE places (
    id TEXT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(5000),
    image_path VARCHAR(255),
    price REAL NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    owner_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);
INSERT INTO places VALUES('6a9faaf8-04c9-4110-9626-8ff97001c84b','Chez Titi','Salut les loulous, my name is Thierry, but please call me Titi, I’m a 49 yo french man and I like meeting new people, new experiences, exploring new feelings. During your stay, be sure that I’ll do everything in my power to make you feel special and comfortable. When you arrive I’ll cook a typical french dinner for you which is baguette and red wine. Then we will enjoy the jacuzzi while drinking a bottle of champagne. After that you’ll relax completely while I’m massaging you and I’ll teach you how to really let go, how to open yourself to the sensuality of the touch. Then we’ll go to bed. In the morning you’ll enjoy the traditional french petit-dejeuner “cafe-clope”, and you’ll be one your way, keeping this night as the best memory of your life ;)','images/Titi.png',10.0,49.3817000000000021,3.32359999999999988,'29f9fcd6-fd2a-4118-ba84-c3b443ba770e','2025-11-20 14:01:02.597949','2025-11-20 14:01:02.597954');
INSERT INTO places VALUES('bd5fd617-140a-4475-96f3-6d4ff0b64c0c','Charming Porcelain Doll House','Come enjoy a good night sleep among hundreds of porcelain dolls staring at you. They never blink… sometimes they move.','images/Doll_House.png',150.0,33.0762,-89.2989000000000032,'7e1554ad-bf66-4460-8126-74ccaaa862e2','2025-11-20 14:18:34.511023','2025-11-20 14:18:34.511028');
INSERT INTO places VALUES('ce42aca7-a740-43c9-9eda-c9381bb35b03','The Smothering Love Nest 💏','We welcome you for a night (or more!) in our little love corner 💖🥰, here no bad vibes allowed 🚫, only love 💏💘. Immerse yourself in our bubble of tenderness and affection 🌸🫂 and leave completely saturated with hugs and love 🤗💞. Upon request, you may also spend the night in our arms 🛏️💋','images/Love_Nest.jpg',25.0,49.5666000000000011,3.61660000000000003,'3d32397a-b3a3-4c0e-bad9-c4df1eaced21','2025-11-20 14:23:40.941479','2025-11-20 14:23:40.941486');
INSERT INTO places VALUES('0d9e335c-2c8d-48c2-87d4-a2ca977cd733','Desperate house with wifi','Please come visit me… I''m terribly lonely these days. The walls don’t answer anymore, and the silence grows heavier every night. I’ve stopped finding joy in anything, and sometimes I wonder if I’m already fading away. Maybe you could sit with me… witness this slow unraveling, this quiet decay. There’s something strangely beautiful in watching a life drift like smoke into the dark. Stay awhile. I don’t want to go alone.','images/Desperate_house.png',5.0,53.4084000000000003,-2.99160000000000003,'595d7df7-c3ea-46ad-ab0f-8dbfdf660db3','2025-11-20 14:29:48.342919','2025-11-20 14:29:48.342925');
COMMIT;
