import { StyleSheet, TextInput, TouchableOpacity } from "react-native";
import axios from "axios";

import EditScreenInfo from "@/components/EditScreenInfo";
import { Text, View } from "@/components/Themed";
import React from "react";

export default function TabOneScreen() {
	const [username, setUsername] = React.useState("");
	const [password, setPassword] = React.useState("");
	const [statusMessage, setStatusMessage] = React.useState("");

	const onPress = async () => {
		try {
			console.log(username, password);

			const response = await axios.post("http://localhost:5000/login", {
				username,
				password,
			});

			console.log(response.data);
			setStatusMessage(response.data.message);
		} catch (error: any) {
			if (error.response) {
				// The request was made and the server responded with a status code
				// that falls out of the range of 2xx
				console.log(error.response.data.message);
			} else {
				// Something happened in setting up the request that triggered an Error
				console.log("Error", error.message);
			}
		}
	};

	return (
		<View style={styles.container}>
			<Text style={styles.title}>Login</Text>
			<Text style={styles.p}>{statusMessage}</Text>
			<View
				style={styles.separator}
				lightColor="#eee"
				darkColor="rgba(255,255,255,0.1)"
			/>
			<TextInput
				style={styles.input}
				onChangeText={setUsername}
				placeholder="Username"
				autoCapitalize="none"
				autoCorrect={false}
				value={username}
			/>
			<TextInput
				style={styles.input}
				onChangeText={setPassword}
				value={password}
				placeholder="Password"
				autoCapitalize="none"
				autoCorrect={false}
				keyboardType="numeric"
			/>
			<TouchableOpacity style={styles.button} onPress={onPress}>
				<Text>Login</Text>
			</TouchableOpacity>
		</View>
	);
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		alignItems: "center",
		justifyContent: "center",
	},
	title: {
		fontSize: 20,
		fontWeight: "bold",
	},
	p: {
		fontSize: 12,
		color: "red",
	},
	separator: {
		marginVertical: 30,
		height: 1,
		width: "80%",
	},
	input: {
		height: 40,
		margin: 12,
		borderWidth: 1,
		padding: 10,
		width: "80%",
	},
	button: {
		alignItems: "center",
		backgroundColor: "#DDDDDD",
		padding: 10,
	},
	countContainer: {
		alignItems: "center",
		padding: 10,
	},
});
