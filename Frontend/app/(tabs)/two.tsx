import { StyleSheet, TextInput, TouchableOpacity } from "react-native";
import axios from "axios";

import EditScreenInfo from "@/components/EditScreenInfo";
import { Text, View } from "@/components/Themed";
import React from "react";

export default function TabTwoScreen() {
	const [username, setUsername] = React.useState("");
	const [password, setPassword] = React.useState("");
	const [statusMessage, setStatusMessage] = React.useState("");
	const onPress = async () => {
		try {
			console.log(username, password);
			const response = await axios.post(
				"http://localhost:5000/register",
				{
					username,
					password,
				}
			);

			console.log(response.data.message);
			setStatusMessage(response.data.message);
		} catch (error: any) {
			console.log(error.message);
		}
		setUsername("");
		setPassword("");
	};

	return (
		<View style={styles.container}>
			<Text style={styles.title}>Register</Text>
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
				value={username}
			/>
			<TextInput
				style={styles.input}
				onChangeText={setPassword}
				value={password}
				placeholder="Password"
				keyboardType="numeric"
			/>
			<TouchableOpacity style={styles.button} onPress={onPress}>
				<Text>Sign Up</Text>
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
